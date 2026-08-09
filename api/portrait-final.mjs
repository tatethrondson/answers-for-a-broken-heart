import { readFileSync } from "node:fs";

export default {
  fetch() {
    const encoded = readFileSync(new URL("../portrait-inline.b64", import.meta.url), "utf8").trim();
    const bytes = Buffer.from(encoded, "base64");

    if (bytes.length < 1000 || bytes[0] !== 0xff || bytes[1] !== 0xd8 || bytes[2] !== 0xff || bytes[bytes.length - 2] !== 0xff || bytes[bytes.length - 1] !== 0xd9) {
      return new Response("Portrait data failed JPEG validation", { status: 500 });
    }

    return new Response(bytes, {
      status: 200,
      headers: {
        "Content-Type": "image/jpeg",
        "Cache-Control": "no-store, max-age=0",
        "Content-Length": String(bytes.byteLength)
      }
    });
  }
};
