const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
  try {
    const parts = ['part01.txt','part02.txt','part03.txt','part04.txt'];
    const b64 = parts.map(name => fs.readFileSync(path.join(process.cwd(), 'portrait_parts', name), 'utf8').trim()).join('');
    const image = Buffer.from(b64, 'base64');

    if (image.length < 1000 || image[0] !== 0xff || image[1] !== 0xd8 || image[image.length - 2] !== 0xff || image[image.length - 1] !== 0xd9) {
      throw new Error('Invalid JPEG payload');
    }

    res.setHeader('Content-Type', 'image/jpeg');
    res.setHeader('Content-Length', String(image.length));
    res.setHeader('Cache-Control', 'no-store, max-age=0');
    res.statusCode = 200;
    res.end(image);
  } catch (err) {
    res.statusCode = 500;
    res.setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('Portrait unavailable');
  }
};
