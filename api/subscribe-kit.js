const KIT_API = 'https://api.kit.com/v4';

const SEGMENT_FORMS = {
  pastoral_notes: 'KIT_FORM_PASTORAL_NOTES',
  guide_2am: 'KIT_FORM_GUIDE_2AM',
  book_launch: 'KIT_FORM_BOOK_LAUNCH',
  church_resources: 'KIT_FORM_CHURCH_RESOURCES',
  launch_team: 'KIT_FORM_LAUNCH_TEAM'
};

function parseBody(req) {
  if (!req.body) return {};
  if (typeof req.body === 'object') return req.body;
  try { return JSON.parse(req.body); } catch (_) {}
  try { return Object.fromEntries(new URLSearchParams(req.body)); } catch (_) {}
  return {};
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || '').trim());
}

async function kitRequest(path, options = {}) {
  const apiKey = process.env.KIT_API_KEY;
  if (!apiKey) throw new Error('KIT_API_KEY is not configured');
  const response = await fetch(`${KIT_API}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'X-Kit-Api-Key': apiKey,
      ...(options.headers || {})
    }
  });
  const text = await response.text();
  let data = {};
  try { data = text ? JSON.parse(text) : {}; } catch (_) { data = { raw: text }; }
  if (!response.ok) {
    const error = new Error(`Kit request failed with ${response.status}`);
    error.status = response.status;
    error.data = data;
    throw error;
  }
  return data;
}

module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store, max-age=0');

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    res.statusCode = 405;
    return res.end(JSON.stringify({ ok: false, error: 'Method not allowed' }));
  }

  const body = parseBody(req);
  const email = String(body.email || body.email_address || '').trim().toLowerCase();
  const firstName = String(body.first_name || body.firstName || '').trim();
  const segment = String(body.segment || '').trim();
  const honey = String(body._honey || body.honey || '').trim();

  // Silently accept bot-filled honeypot submissions without sending them to Kit.
  if (honey) {
    res.statusCode = 200;
    return res.end(JSON.stringify({ ok: true }));
  }

  if (!isEmail(email)) {
    res.statusCode = 400;
    return res.end(JSON.stringify({ ok: false, error: 'Please enter a valid email address.' }));
  }

  if (!SEGMENT_FORMS[segment]) {
    res.statusCode = 400;
    return res.end(JSON.stringify({ ok: false, error: 'Unknown subscription segment.' }));
  }

  if (segment === 'launch_team' && process.env.KIT_ENABLE_LAUNCH_TEAM !== 'true') {
    res.statusCode = 403;
    return res.end(JSON.stringify({ ok: false, error: 'Launch-team signup is not enabled.' }));
  }

  const formEnv = SEGMENT_FORMS[segment];
  const formId = process.env[formEnv];
  if (!process.env.KIT_API_KEY || !formId) {
    res.statusCode = 503;
    return res.end(JSON.stringify({ ok: false, error: 'Email signup is not configured yet.' }));
  }

  try {
    await kitRequest('/subscribers', {
      method: 'POST',
      body: JSON.stringify({
        email_address: email,
        ...(firstName ? { first_name: firstName } : {})
      })
    });

    const referrer = String(req.headers.referer || '').slice(0, 1000) || null;
    await kitRequest(`/forms/${encodeURIComponent(formId)}/subscribers`, {
      method: 'POST',
      body: JSON.stringify({
        email_address: email,
        ...(referrer ? { referrer } : {})
      })
    });

    res.statusCode = 200;
    return res.end(JSON.stringify({ ok: true, segment }));
  } catch (err) {
    console.error('Kit subscription error', err && err.status, err && err.data ? err.data : err);
    res.statusCode = 502;
    return res.end(JSON.stringify({ ok: false, error: 'We could not save your signup right now.' }));
  }
};
