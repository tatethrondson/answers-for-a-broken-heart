import legacyPortrait from './portrait-final.mjs';

export default async function handler(req, res) {
  try {
    const response = await legacyPortrait.fetch();
    const bytes = Buffer.from(await response.arrayBuffer());

    if (bytes.length < 1000 || bytes[0] !== 0xff || bytes[1] !== 0xd8 || bytes[bytes.length - 2] !== 0xff || bytes[bytes.length - 1] !== 0xd9) {
      throw new Error(`Invalid JPEG payload (${bytes.length} bytes)`);
    }

    res.statusCode = 200;
    res.setHeader('Content-Type', 'image/jpeg');
    res.setHeader('Content-Length', String(bytes.length));
    res.setHeader('Cache-Control', 'no-store, max-age=0');
    res.end(bytes);
  } catch (error) {
    console.error(error);
    res.statusCode = 500;
    res.setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('Portrait rendering failed');
  }
}
