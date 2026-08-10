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

  document.addEventListener('click',function(e){
    var a=e.target.closest('a,button');
    if(!a) return;
    var href=a.getAttribute('href') || '';
    var label=text(a);

    if(href==='/start-here') track('Start Here Click',{page:page(),label:label});
    if(href==='/what-hurts-today') track('What Hurts Today Click',{page:page(),label:label});
    if(href==='/church-resources') track('Church Resources Click',{page:page(),label:label});
    if(href==='/2am-guide') track('2AM Guide Opened',{page:page(),label:label});
    if(href.indexOf('view=book')!==-1) track('Book Interest Click',{page:page(),label:label});
    if((href.indexOf('youtube.com')!==-1 || href.indexOf('youtu.be')!==-1) && (a.closest('.answerJourney') || a.closest('.podcastResource'))){
      track('Podcast Resource Click',{page:page(),label:label});
    }
    if(a.classList && a.classList.contains('shareBtn')){
      track('Answer Shared',{page:page(),method:label});
    }
    if(a.closest && a.closest('.answerTopicHub')){
      track('Topic Guide Click',{page:page(),label:label});
    }
  });

  document.addEventListener('submit',function(e){
    var form=e.target;
    if(!form || form.tagName!=='FORM') return;
    var interest=form.querySelector('input[name="interest"]');
    var value=interest ? interest.value : '';
    if(value.indexOf('2:00 A.M. Guide')!==-1) track('2AM Guide Signup',{page:page()});
    else if(value.indexOf('book launch list')!==-1) track('Book Launch Signup',{page:page()});
    else if(value.indexOf('Church and Pastor Resources')!==-1) track('Church Resources Signup',{page:page()});
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
