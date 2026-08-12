(()=>{
  const m=(location.pathname.match(/^\/answer-(\d{2})(?:\.html)?$/)||[])[1];
  if(!m) return;
  const n=parseInt(m,10);
  const cat={
    1:'God Feels Far Away',2:'God Feels Far Away',3:'God Feels Far Away',9:'God Feels Far Away',10:'God Feels Far Away',
    4:'Suffering & Why',5:'Suffering & Why',6:'Suffering & Why',7:'Suffering & Why',8:'Suffering & Why',
    14:'Grief & Loss',15:'Grief & Loss',16:'Grief & Loss',17:'Grief & Loss',
    11:'Anger & Unanswered Prayer',13:'Anger & Unanswered Prayer',18:'Anger & Unanswered Prayer',19:'Anger & Unanswered Prayer',
    12:'Relational Hurt & Forgiveness',20:'Relational Hurt & Forgiveness',21:'Relational Hurt & Forgiveness',22:'Relational Hurt & Forgiveness',
    23:'Doubt & Church Hurt',24:'Doubt & Church Hurt'
  };
  const short={
    1:'He’s always been there.',
    2:'He showed you His face.',
    3:'Some things become clearer looking back.',
    4:'This is not the world God called very good.',
    5:'Honest questions are not unbelief.',
    6:'Your view is not the whole story.',
    7:'God can redeem even this.',
    8:'Sometimes He gives you Himself instead of an explanation.',
    9:'He wept with you.',
    10:'He entered it—and He will end it.',
    11:'His silence isn’t His approval.',
    12:'Your pain and their guilt are not the same conversation.',
    13:'A no is not the end of the story.',
    14:'Death does not get the final word.',
    15:'You’re allowed to grieve as long as it takes.',
    16:'When you’re ready, ask a different question.',
    17:'Healing is not a straight line.',
    18:'Anger at God is not the opposite of faith.',
    19:'Bring Him the real prayer, not the polished one.',
    20:'To be loved is to be woundable.',
    21:'Forgiveness releases vengeance without calling the wrong right.',
    22:'Forgiveness is not reconciliation.',
    23:'Separate Jesus from what was done in His name.',
    24:'Your doubt is not disqualifying.'
  };
  const topic={
    'god-feels-far-away':'God Feels Far Away',
    'why-god-allows-suffering':'Suffering & Why',
    'grief-and-loss':'Grief & Loss',
    'anger-and-unanswered-prayer':'Anger & Unanswered Prayer',
    'forgiveness-and-relational-hurt':'Relational Hurt & Forgiveness',
    'doubt-and-church-hurt':'Doubt & Church Hurt'
  };

  function numFromHref(href){const x=(href||'').match(/\/answer-(\d{2})/);return x?parseInt(x[1],10):0;}
  function apply(){
    const hero=document.querySelector('main>.hero .eyebrow');
    if(hero && cat[n]) hero.textContent=`Answer ${m} · ${cat[n]}`;

    const sh=document.querySelector('#short h2,.short h2');
    if(sh && short[n]) sh.textContent=short[n];

    if(n===3){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='Some of God’s work becomes clearer in hindsight, while some questions may remain unresolved in this life.';
    }
    if(n===4){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='You are not wrong for feeling that something about this world is terribly wrong. Scripture says the brokenness we know is not the world God called very good.';
    }
    if(n===6){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='Sometimes God does not give us the explanation we want. Limited perspective is not proof that He has stopped being wise, good, or present.';
    }
    if(n===10){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='Jesus did more than enter human suffering. In His death and resurrection, He guaranteed that suffering and death will not have the final word.';
    }
    if(n===21){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='Forgiveness is not saying the wound was small. It is releasing personal vengeance to God without surrendering truth, justice, or wise boundaries.';
    }
    if(n===23){
      const dek=document.querySelector('main>.hero .dek');
      if(dek) dek.textContent='Before you decide what to do with faith, separate Jesus from the hypocrisy, abuse, legalism, or disappointment people may have attached to His name.';
    }

    document.querySelectorAll('.answerTopicHub a[href]').forEach(a=>{
      const slug=(a.getAttribute('href')||'').replace(/^\//,'').replace(/\/$/,'');
      if(topic[slug]) a.textContent=topic[slug]+' →';
    });

    document.querySelectorAll('.relatedCard').forEach(card=>{
      const k=numFromHref(card.getAttribute('href'));
      if(!k) return;
      const small=card.querySelector('small');
      if(small && cat[k]) small.textContent=`Answer ${String(k).padStart(2,'0')} · ${cat[k]}`;
      const span=card.querySelector('span');
      if(span && short[k]) span.textContent=short[k].replace(/[.]$/,'')+' →';
    });

    document.querySelectorAll('.next a').forEach(a=>{
      const k=numFromHref(a.getAttribute('href'));
      if(!k) return;
      const small=a.querySelector('small');
      if(small && cat[k]) small.textContent=`ANSWER ${String(k).padStart(2,'0')} · ${cat[k].toUpperCase()}`;
      const p=a.querySelector('p');
      if(p && short[k]) p.textContent=short[k].replace(/[.]$/,'')+' →';
    });

    document.querySelectorAll('a[href="/?view=book"],a[href="?view=book"]').forEach(a=>a.setAttribute('href','/book'));
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply); else apply();
  setTimeout(apply,120);setTimeout(apply,500);
  new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
})();
