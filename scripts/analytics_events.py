from pathlib import Path
import re

START='<!-- CONVERSION-ANALYTICS-START -->'
END='<!-- CONVERSION-ANALYTICS-END -->'

SCRIPT=r'''<!-- CONVERSION-ANALYTICS-START -->
<script>
(function(){
  function track(name,data){
    try{
      if(typeof window.va==='function'){
        window.va('event',{name:name,data:data||{}});
      }
    }catch(e){}
  }
  function page(){ return window.location.pathname || '/'; }
  function text(el){ return (el && el.textContent ? el.textContent : '').trim().replace(/\s+/g,' ').slice(0,80); }
  function destinationLabel(a){
    var heading=a && a.querySelector ? a.querySelector('h3,strong') : null;
    return text(heading) || text(a);
  }

  document.addEventListener('click',function(e){
    var a=e.target.closest('a,button');
    if(!a) return;
    var href=a.getAttribute('href') || '';
    var label=text(a);
    var current=page();

    if(href==='/start-here') track('Start Here Click',{page:current,label:label});
    if(href==='/all-answers') track('24 Answers Click',{page:current,label:label});
    if(href==='/what-hurts-today') track('What Hurts Today Click',{page:current,label:label});
    if(href==='/church-resources') track('Church Resources Click',{page:current,label:label});

    if(href==='/2am-guide'){
      track('2AM Guide Opened',{page:current,label:label});
      track('Free Guide Click',{page:current,guide:'2am-guide'});
    }
    if(href==='/can-christians-be-depressed') track('Free Guide Click',{page:current,guide:'depression'});
    if(href==='/help-someone') track('Free Guide Click',{page:current,guide:'help-someone'});

    if(href==='/book' || href.indexOf('view=book')!==-1){
      track('Book Interest Click',{page:current,label:label});
    }
    if(current==='/book' && href==='#book-updates'){
      track('Book Release Updates Click',{page:current,label:label});
    }

    if(current==='/start-here' && a.closest && a.closest('.choice')){
      track('Start Here Choice',{page:current,destination:href,label:destinationLabel(a)});
    }
    if(current==='/all-answers' && /^\/answer-\d{2}$/.test(href) && a.closest && a.closest('.card')){
      track('Answer Opened',{page:current,answer:href,label:destinationLabel(a)});
    }
    if(current==='/all-answers' && a.classList && a.classList.contains('filter')){
      track('Answers Filter',{page:current,label:label});
    }
    if(/^\/answer-\d{2}$/.test(current) && a.closest && a.closest('.journeyCard')){
      track('Answer Next Step',{page:current,destination:href,label:destinationLabel(a)});
    }

    if((href.indexOf('youtube.com')!==-1 || href.indexOf('youtu.be')!==-1) && (a.closest('.answerJourney') || a.closest('.podcastResource'))){
      track('Podcast Resource Click',{page:current,label:label});
    }
    if(a.classList && a.classList.contains('shareBtn')){
      track('Answer Shared',{page:current,method:label});
    }
    if(a.closest && a.closest('.answerTopicHub')){
      track('Topic Guide Click',{page:current,label:label});
    }
  });

  var searchTracked=false;
  document.addEventListener('input',function(e){
    var input=e.target;
    if(searchTracked || page()!=='/all-answers' || !input || input.id!=='answerSearch') return;
    if((input.value || '').trim().length>=3){
      searchTracked=true;
      // Deliberately do not send the search text. Hurt-related searches can be sensitive.
      track('Answers Search Used',{page:page()});
    }
  },true);

  document.addEventListener('submit',function(e){
    var form=e.target;
    if(!form || form.tagName!=='FORM') return;
    var interest=form.querySelector('input[name="interest"]');
    var value=interest ? interest.value : '';
    var lower=value.toLowerCase();
    if(lower.indexOf('2:00 a.m. guide')!==-1) track('2AM Guide Signup',{page:page()});
    else if(lower.indexOf('book launch list')!==-1 || lower.indexOf('release notification')!==-1) track('Book Launch Signup',{page:page()});
    else if(lower.indexOf('church and pastor resources')!==-1) track('Church Resources Signup',{page:page()});
  },true);

  if(/^\/answer-\d{2}$/.test(page())){
    var sent=false;
    window.addEventListener('scroll',function(){
      if(sent) return;
      var doc=document.documentElement;
      var max=Math.max(1,doc.scrollHeight-window.innerHeight);
      if(window.scrollY/max>=0.5){
        sent=true;
        track('Answer 50% Read',{page:page()});
      }
    },{passive:true});
  }
})();
</script>
<!-- CONVERSION-ANALYTICS-END -->'''

for p in Path('.').glob('*.html'):
    s=p.read_text(encoding='utf-8')
    s=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',s,flags=re.S)
    if '</body>' not in s:
        continue
    s=s.replace('</body>',SCRIPT+'\n</body>',1)
    p.write_text(s,encoding='utf-8')
    print('Instrumented',p)
