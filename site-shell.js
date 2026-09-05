(()=>{
  const ITEMS=[
    ['Start Here','/start-here'],
    ['24 Answers','/all-answers'],
    ['Free Resources','/free-guides'],
    ['The Book','/book'],
    ['About','/about']
  ];
  const SITE_HREFS=new Set(['/','/start-here','/begin-here','/what-hurts-today','/all-answers','/free-guides','/book','/about','/contact','/church-resources']);

  const FINAL_ANSWERS={
    1:{title:'He’s Always Been There',summary:'Pain can make God difficult to recognize, but it does not mean He has been absent. Sometimes faith begins by noticing that He was nearer than you knew.'},
    2:{title:'He Wants to Be Known',summary:'God has not asked you to trust a stranger. Creation points to Him, Scripture tells us who He is, and Jesus shows us His heart.'},
    3:{title:'You Don’t Have the Whole Story Yet',summary:'What you can see right now is real, but it is not the whole story. God can be at work in a chapter you do not yet understand.'},
    4:{title:'This Is Not the World He Made',summary:'The Bible does not ask you to call suffering good. It tells us something has gone terribly wrong with the world—and that God will not leave it broken forever.'},
    5:{title:'Honest Questions Are Not Unbelief',summary:'Faith is not pretending you have no questions. Scripture is full of faithful people who brought their confusion, grief, and even protest directly to God.'},
    6:{title:'He Sees What You Can’t See',summary:'You may never receive the explanation you want. But limited understanding is not proof that God has lost control, stopped being good, or ceased to see what you cannot.'},
    7:{title:'“All Things — Even This”',summary:'Romans 8:28 does not call every painful thing good. It promises that God is able to work even through what we would never have chosen.'},
    8:{title:'Sometimes He Gives You Himself Instead of an Explanation',summary:'Sometimes the explanation never comes. Christianity does not promise an answer for every mystery, but it gives us a God who comes near in the middle of it.'},
    9:{title:'He Wept With You',summary:'Jesus does not watch grief from a safe distance. He entered human sorrow, stood beside a grave, and wept with people He loved.'},
    10:{title:'The Ending Has Already Been Settled',summary:'Jesus did more than enter suffering. His death and resurrection mean pain gets a chapter and death gets a chapter—but neither gets the last one.'},
    11:{title:'His Silence Isn’t His Approval',summary:'Someone may appear to prosper after doing real harm. That does not mean God has missed it, approved it, or forgotten what happened.'},
    12:{title:'Their Guilt Is Not Yours to Carry',summary:'You can own your own sin without taking responsibility for what someone else chose to do to you. Shared imperfection does not create shared responsibility.'},
    13:{title:'A “No” Is Not the End of the Story',summary:'An unanswered prayer can break your heart without proving that God did not hear you. His “no” is not proof that He has stopped working.'},
    14:{title:'Death Does Not Get the Final Word',summary:'Death is real, painful, and an enemy. But because Jesus rose, the grave is not the end of the Christian story.'},
    15:{title:'You’re Allowed to Grieve as Long as It Takes',summary:'The calendar can move much faster than a broken heart does. Scripture gives sorrow room and does not shame you for still missing someone you loved.'},
    16:{title:'Maybe “Why?” Isn’t the Only Question',summary:'You may need to ask why for a while. When you are ready, another question can begin to open: What can God still do with what remains?'},
    17:{title:'Grief Needs Somewhere to Go',summary:'Grief does not need to be rushed, but it does need somewhere to go. You can carry it honestly toward God instead of letting it harden in isolation.'},
    18:{title:'Anger at God Is Not the Opposite of Faith',summary:'Anger does not automatically mean faith has disappeared. Sometimes faith sounds like refusing to stop talking to God in the dark.'},
    19:{title:'Bring Him the Real Prayer, Not the Polished One',summary:'God does not need a cleaned-up version of your prayer. Bring Him the fear, anger, confusion, silence, and tears you are actually carrying.'},
    20:{title:'Real Love Carries Real Risk',summary:'The people close enough to help us deeply are also close enough to hurt us deeply. The answer to being wounded is not to become unreachable.'},
    21:{title:'You Don’t Need Their Apology to Be Free',summary:'Their repentance belongs to them. Your decision to release the debt to God does not have to wait for an apology that may never come.'},
    22:{title:'Forgiveness Doesn’t Mean Reopening the Door',summary:'Forgiveness and reconciliation are not the same thing. You can release bitterness while still keeping wise boundaries and allowing trust to rebuild slowly.'},
    23:{title:'Look at Jesus Again',summary:'Pain, hypocrisy, and bad theology can distort the picture of God. When you wonder what He is really like, look again at Jesus.'},
    24:{title:'You Can Trust Him With What You Still Don’t Understand',summary:'There will always be another question. You do not have to solve every mystery before you keep walking with the God who has shown you His heart in Jesus.'}
  };

  const OLD_TITLES={
    'He Showed You His Face':'He Wants to Be Known',
    'You’ll See It Looking Back':'You Don’t Have the Whole Story Yet',
    'He Knows More Than You Do':'He Sees What You Can’t See',
    'He Didn’t Just Enter It — He Ended It':'The Ending Has Already Been Settled',
    'Your Pain and Their Guilt Are Not the Same Conversation':'Their Guilt Is Not Yours to Carry',
    'Ask a Different Question':'Maybe “Why?” Isn’t the Only Question',
    'Grief That Stops Moving Becomes Bitterness':'Grief Needs Somewhere to Go',
    'To Be Loved Is to Be Woundable':'Real Love Carries Real Risk',
    'Forgiving Them Lets You Look Like Your Father':'You Don’t Need Their Apology to Be Free',
    'Forgiveness Is Not Reconciliation':'Forgiveness Doesn’t Mean Reopening the Door',
    'Make Sure You’re Rejecting the Real Thing':'Look at Jesus Again',
    'Your Doubt Is Not Disqualifying':'You Can Trust Him With What You Still Don’t Understand'
  };

  function ensureConsistencyStyles(){
    if(document.querySelector('link[href^="/site-consistency-v1.css"]')) return;
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href='/site-consistency-v1.css?v=1';
    document.head.appendChild(link);
  }

  function normalizePath(p){
    if(!p||p==='/') return '/';
    return p.replace(/\.html$/,'').replace(/\/$/,'')||'/';
  }
  function isActive(href){
    const here=normalizePath(window.location.pathname);
    const target=normalizePath(href);
    if(target==='/start-here'&&(here==='/begin-here'||here==='/what-hurts-today')) return true;
    return here===target;
  }
  function links(){
    return ITEMS.map(([label,href])=>`<a href="${href}"${isActive(href)?' aria-current="page"':''}>${label}</a>`).join('');
  }
  function headerMarkup(){
    return `<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation">${links()}</nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation">${links()}</nav></details></div>`;
  }
  function hasSiteLinks(el){
    return [...el.querySelectorAll('a[href]')].some(a=>SITE_HREFS.has(normalizePath(a.getAttribute('href'))));
  }
  function beforeMain(el,main){
    if(!main) return true;
    if(main.contains(el)) return false;
    return !!(el.compareDocumentPosition(main)&Node.DOCUMENT_POSITION_FOLLOWING);
  }
  function enforce(){
    const body=document.body;
    if(!body) return;
    ensureConsistencyStyles();
    const main=document.querySelector('main');

    let header=document.querySelector('header.siteShellHeader');
    if(!header){
      header=document.createElement('header');
      header.className='siteShellHeader';
    }

    document.querySelectorAll('header').forEach(h=>{
      if(h===header) return;
      if(beforeMain(h,main)&&hasSiteLinks(h)) h.remove();
    });
    document.querySelectorAll('nav').forEach(nav=>{
      if(header.contains(nav)) return;
      if(beforeMain(nav,main)&&hasSiteLinks(nav)) nav.remove();
    });

    if(body.firstElementChild!==header) body.insertBefore(header,body.firstChild);
    header.className='siteShellHeader';
    header.innerHTML=headerMarkup();

    header.querySelectorAll('.siteShellMobileMenu a').forEach(a=>a.addEventListener('click',()=>{
      const d=header.querySelector('.siteShellMobile');
      if(d) d.open=false;
    }));

    if(!document.getElementById('site-shell-runtime-guard')){
      const style=document.createElement('style');
      style.id='site-shell-runtime-guard';
      style.textContent=`
        body>header.siteShellHeader{display:block!important}
        .siteShellHeader .siteShellLinks{display:flex!important}
        .siteShellHeader .siteShellMobile{display:none!important}
        @media(max-width:760px){
          .siteShellHeader .siteShellLinks{display:none!important}
          .siteShellHeader .siteShellMobile{display:block!important}
        }
      `;
      document.head.appendChild(style);
    }
  }

  function answerNumber(){
    const m=(document.body&&document.body.className||'').match(/page-answer-(\d{2})/);
    if(m) return Number(m[1]);
    const p=normalizePath(location.pathname).match(/\/answer-(\d{2})$/);
    return p?Number(p[1]):null;
  }

  function replaceOldTitles(root=document.body){
    if(!root) return;
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    const nodes=[];
    while(walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node=>{
      let value=node.nodeValue;
      let next=value;
      Object.entries(OLD_TITLES).forEach(([oldTitle,newTitle])=>{next=next.split(oldTitle).join(newTitle)});
      if(next!==value) node.nodeValue=next;
    });
  }

  function syncHomepage(){
    if(normalizePath(location.pathname)!=='/') return;
    const promise=document.querySelector('.promise span:last-child');
    if(promise) promise.textContent='Biblical truth. Honest questions. Hope in Christ.';
    const intro=document.querySelector('.hurts .centerIntro');
    if(intro) intro.innerHTML='Pain has a way of isolating us. You don’t have to walk through it alone.<br>Find a biblical place to begin.';
    const bridge=document.querySelector('.bookBridgeCopy p');
    if(bridge) bridge.innerHTML='<em>Answers for a Broken Heart</em> walks through 24 questions people ask when pain makes easy answers feel too small. The website can help you find a place to begin. The book goes deeper into the stories, Scripture, questions, and hope behind those answers.';
    document.querySelectorAll('.coverSub,.bookSub').forEach(el=>{el.innerHTML='Finding God’s Goodness in<br>Grief, Doubt, and Unanswered Prayer'});
  }

  function syncAnswerCopy(){
    const n=answerNumber();
    if(!n||!FINAL_ANSWERS[n]) return;
    const data=FINAL_ANSWERS[n];
    const short=document.querySelector('.article .short, .article .shortAnswer');
    if(short){
      const h=short.querySelector('h2,h3');
      const p=short.querySelector('p:not(.eyebrow)');
      if(h) h.textContent=data.title;
      if(p) p.textContent=data.summary;
    }
    replaceOldTitles(document.body);
  }

  function simplifyAnswerPage(){
    const n=answerNumber();
    if(!n||document.body.dataset.answerSimplified==='1') return;
    const article=document.querySelector('article.article');
    if(!article) return;
    document.body.dataset.answerSimplified='1';

    const start=article.querySelector('.answerSafety')||article.querySelector('.minuteHelp')||article.querySelector('.short')||article.querySelector('.shortAnswer');
    const stop=article.querySelector('.answerDeepDive')||article.querySelector('.answerJourney');
    if(start&&stop&&start.nextSibling&&start.nextSibling!==stop){
      const details=document.createElement('details');
      details.className='siteFullAnswer';
      const summary=document.createElement('summary');
      summary.innerHTML='<span><strong>Read the fuller answer</strong><small>Take your time. Open this when you want to go a little deeper.</small></span><span aria-hidden="true">+</span>';
      const body=document.createElement('div');
      body.className='siteFullAnswerBody';
      details.append(summary,body);
      article.insertBefore(details,start.nextSibling);
      let node=details.nextSibling;
      while(node&&node!==stop){
        const next=node.nextSibling;
        body.appendChild(node);
        node=next;
      }
    }

    const journey=article.querySelector('.answerJourney');
    if(journey&&!journey.closest('.siteNextSteps')){
      const details=document.createElement('details');
      details.className='siteNextSteps';
      const summary=document.createElement('summary');
      summary.innerHTML='<span><strong>Where should I go next?</strong><small>More help, related resources, and ways to keep going.</small></span><span aria-hidden="true">+</span>';
      journey.parentNode.insertBefore(details,journey);
      details.append(summary,journey);
    }

    const side=document.querySelector('.side');
    if(side){
      side.innerHTML='<div class="siteSimpleSide"><p class="eyebrow">Need a different starting point?</p><h3>Start where it hurts.</h3><p>You do not have to work through these answers in order.</p><a href="/start-here">Tell me where it hurts →</a><a href="/all-answers">Browse all 24 answers →</a></div>';
    }

    if(!document.getElementById('answer-simplify-style')){
      const style=document.createElement('style');
      style.id='answer-simplify-style';
      style.textContent=`
        body[class*="page-answer-"] .siteFullAnswer,
        body[class*="page-answer-"] .siteNextSteps{margin:22px 0;border:1px solid #ded8cd;background:#faf8f3}
        body[class*="page-answer-"] .siteFullAnswer>summary,
        body[class*="page-answer-"] .siteNextSteps>summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:18px;padding:20px 22px;color:#183024}
        body[class*="page-answer-"] .siteFullAnswer>summary::-webkit-details-marker,
        body[class*="page-answer-"] .siteNextSteps>summary::-webkit-details-marker{display:none}
        body[class*="page-answer-"] .siteFullAnswer>summary strong,
        body[class*="page-answer-"] .siteNextSteps>summary strong{display:block;font:400 1.28rem/1.2 Georgia,"Times New Roman",serif;color:#183024}
        body[class*="page-answer-"] .siteFullAnswer>summary small,
        body[class*="page-answer-"] .siteNextSteps>summary small{display:block;margin-top:4px;font-size:.76rem;color:#657068}
        body[class*="page-answer-"] .siteFullAnswerBody{padding:8px 24px 28px;border-top:1px solid #ded8cd;background:#fffefb}
        body[class*="page-answer-"] .siteNextSteps>.answerJourney{margin:0!important;border:0!important}
        body[class*="page-answer-"] .siteSimpleSide{border:1px solid #ded8cd;background:#fff;padding:22px}
        body[class*="page-answer-"] .siteSimpleSide h3{margin:4px 0 8px;font:400 1.35rem/1.2 Georgia,"Times New Roman",serif;color:#183024}
        body[class*="page-answer-"] .siteSimpleSide p:not(.eyebrow){font-size:.82rem;line-height:1.55;color:#657068;margin:0 0 12px}
        body[class*="page-answer-"] .siteSimpleSide a{display:block;padding:7px 0;text-decoration:none;font-size:.79rem;font-weight:800;color:#294533}
        body[class*="page-answer-"] section.cta{display:none!important}
        @media(max-width:820px){body[class*="page-answer-"] .siteFullAnswerBody{padding:6px 20px 24px}}
      `;
      document.head.appendChild(style);
    }
  }

  function runContentSync(){
    try{
      replaceOldTitles(document.body);
      syncHomepage();
      syncAnswerCopy();
      simplifyAnswerPage();
    }catch(e){console.error('content sync failed',e)}
  }

  const run=()=>{try{enforce();runContentSync()}catch(e){console.error('site shell enforcement failed',e)}};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',run,{once:true});
  else run();
  window.addEventListener('load',run,{once:true});
  setTimeout(run,50);
  setTimeout(run,350);
  setTimeout(run,1200);

  const observer=new MutationObserver(()=>{setTimeout(runContentSync,0)});
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>observer.observe(document.body,{childList:true,subtree:true}),{once:true});
  else if(document.body) observer.observe(document.body,{childList:true,subtree:true});
})();