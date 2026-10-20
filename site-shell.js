(()=>{
  const HEADER_LOGO='data:image/webp;base64,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';
  const ITEMS=[
    ['Find Help','/start-here'],
    ['Free Resources','/free-guides'],
    ['The Book','/book']
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
    return `<div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><img class="siteShellBrandLogo" src="${HEADER_LOGO}" alt="answers — FOR A BROKEN HEART" width="248" height="76" decoding="async"></a><nav class="siteShellLinks" aria-label="Main navigation">${links()}</nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation">${links()}</nav></details></div>`;
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
    if(!root || document.body?.classList.contains('page-doubt-resource')) return;
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    const nodes=[];
    while(walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(node=>{
      let next=node.nodeValue;
      Object.entries(OLD_TITLES).forEach(([oldTitle,newTitle])=>{next=next.split(oldTitle).join(newTitle)});
      if(next!==node.nodeValue) node.nodeValue=next;
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
    if(!n || document.body.dataset.answerSimplified==='5') return;
    const article=document.querySelector('article.article');
    if(!article) return;
    document.body.dataset.answerSimplified='5';

    if(!document.querySelector('link[href^="/answer-simple-v5.css"]')){
      const css=document.createElement('link');
      css.rel='stylesheet';
      css.href='/answer-simple-v5.css?v=20261020-podcasts';
      document.head.appendChild(css);
    }

    const short=article.querySelector('.short, .shortAnswer');
    const minute=article.querySelector('.minuteHelp');
    const safety=article.querySelector('.answerSafety');
    if(minute){
      const h=minute.querySelector('.minuteHelpHead h2');
      if(h)h.textContent='One Scripture. One next step.';
      const sub=minute.querySelector('.minuteHelpHead span');
      if(sub)sub.remove();
      const grid=minute.querySelector('.minuteGrid');
      if(grid){
        const items=[...grid.children].filter(el=>el.classList.contains('minuteItem'));
        if(items.length>=3){
          const prayerDetails=document.createElement('details');
          prayerDetails.className='sitePrayer';
          const summary=document.createElement('summary');
          summary.textContent='A short prayer for this moment +';
          prayerDetails.append(summary,items[1]);
          grid.insertAdjacentElement('afterend',prayerDetails);
        }
      }
    }

    // The short answer, one Scripture, next step, and safety link stay visible.
    // Other online pastoral reflections are optional, not presented as verbatim book text.
    const anchor=safety||minute||short;
    const journey=article.querySelector('.answerJourney');
    const podcast=article.querySelector('.podcastResource');
    let stop=journey||podcast;
    if(journey&&podcast)stop=(journey.compareDocumentPosition(podcast)&Node.DOCUMENT_POSITION_FOLLOWING)?journey:podcast;
    if(anchor){
      const details=document.createElement('details');
      details.className='siteFullAnswer';
      const summary=document.createElement('summary');
      summary.innerHTML='<span><strong>Read more, if you would like</strong><small>Additional biblical teaching and pastoral reflection.</small></span><span aria-hidden="true">+</span>';
      const body=document.createElement('div');
      body.className='siteFullAnswerBody';
      details.append(summary,body);
      anchor.insertAdjacentElement('afterend',details);
      let sibling=details.nextSibling;
      let moved=0;
      while(sibling&&sibling!==stop){
        const next=sibling.nextSibling;
        body.appendChild(sibling);
        sibling=next;
        moved++;
      }
      if(moved===0)details.remove();
    }

    // Keep episode cards with their thumbnails visible, rather than hiding them
    // in the general "More resources" drawer. Other extras may remain optional.
    const extras=[...article.querySelectorAll('.answerJourney')].filter(el=>!el.closest('.siteFullAnswer'));
    if(extras.length){
      const details=document.createElement('details');
      details.className='siteNextSteps';
      const summary=document.createElement('summary');
      summary.innerHTML='<span><strong>More resources, if you need them</strong><small>Related answers, conversations, and ways to stay connected.</small></span><span aria-hidden="true">+</span>';
      const body=document.createElement('div');
      body.className='siteNextStepsBody';
      details.append(summary,body);
      extras[0].parentNode.insertBefore(details,extras[0]);
      extras.forEach(el=>body.appendChild(el));
    }

    // Surface the original podcast card near the brief answer, preserving
    // its image, title, description, and exact YouTube destination.
    const featuredPodcasts=[...article.querySelectorAll('.podcastResource')].filter(el=>!el.closest('.siteFullAnswer')&&!el.closest('.siteNextSteps'));
    const readingDetails=article.querySelector('.siteFullAnswer');
    if(featuredPodcasts.length){
      featuredPodcasts.forEach((episode,i)=>{
        episode.classList.add('siteFeaturedPodcast');
        if(readingDetails){
          readingDetails.insertAdjacentElement('beforebegin',episode);
        }else if(anchor){
          anchor.insertAdjacentElement('afterend',episode);
        }
      });
    }

    const side=document.querySelector('.side');
    if(side)side.setAttribute('aria-hidden','true');
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