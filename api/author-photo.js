const fs = require('fs');
const path = require('path');

module.exports = function handler(req, res) {
  try {
    const dir = path.join(process.cwd(), 'portrait-hires');
    const names = fs.readdirSync(dir).filter(name => /^part\d+\.b64$/.test(name)).sort();
    if (!names.length) throw new Error('No portrait source parts found');

    const outerBase64 = names.map(name => fs.readFileSync(path.join(dir, name), 'utf8').trim()).join('');
    const outerBytes = Buffer.from(outerBase64, 'base64');

    let jpeg;
    // If the stored source is already a JPEG, serve it directly.
    if (outerBytes.length > 2 && outerBytes[0] === 0xff && outerBytes[1] === 0xd8) {
      jpeg = outerBytes;
    } else {
      // Current source is an SVG wrapper around the real JPEG. Extract the inner JPEG bytes.
      const wrapper = outerBytes.toString('utf8');
      const match = wrapper.match(/data:image\/jpeg;base64,([^"'\s<]+)/i);
      if (!match) throw new Error('Embedded JPEG not found in portrait source');
      jpeg = Buffer.from(match[1], 'base64');
    }

    if (!(jpeg.length > 2 && jpeg[0] === 0xff && jpeg[1] === 0xd8)) {
      throw new Error('Decoded portrait is not a valid JPEG');
    }

    res.setHeader('Content-Type', 'image/jpeg');
    res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=86400, stale-while-revalidate=604800');
    res.setHeader('Content-Length', String(jpeg.length));
    res.status(200).send(jpeg);
  } catch (error) {
    console.error('Author photo error:', error);
    res.status(500).setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('Author photo unavailable');
  }
};
