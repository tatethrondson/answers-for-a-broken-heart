const fs = require('fs');
const path = require('path');

module.exports = function handler(req, res) {
  try {
    const parts = [
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part01.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part02.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part03.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part04.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part05.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part06.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part07.b64'), 'utf8').trim(),
      fs.readFileSync(path.join(process.cwd(), 'portrait-hires', 'part08.b64'), 'utf8').trim()
    ];

    const decoded = Buffer.from(parts.join(''), 'base64');
    let jpeg = decoded;

    // Backward-compatible fallback in case the checked-in source is ever wrapped in SVG.
    if (!(decoded.length > 2 && decoded[0] === 0xff && decoded[1] === 0xd8)) {
      const wrapper = decoded.toString('utf8');
      const match = wrapper.match(/data:image\/jpeg;base64,([^"'\s<]+)/i);
      if (!match) throw new Error('Valid JPEG portrait not found');
      jpeg = Buffer.from(match[1], 'base64');
    }

    if (!(jpeg.length > 2 && jpeg[0] === 0xff && jpeg[1] === 0xd8)) {
      throw new Error('Decoded portrait is not a valid JPEG');
    }

    res.setHeader('Content-Type', 'image/jpeg');
    res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=86400, stale-while-revalidate=604800');
    res.status(200).send(jpeg);
  } catch (error) {
    console.error('Author photo error:', error);
    res.status(500).setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('Author photo unavailable');
  }
};
