(()=>{
  function isHomepage(){
    const params=new URLSearchParams(location.search);
    return location.pathname==='/' && !params.has('view') && !params.has('answer');
  }

  function apply(){
    if(!isHomepage()) return;
    let style=document.getElementById('ab-home-image-variety');
    if(!style){
      style=document.createElement('style');
      style.id='ab-home-image-variety';
      document.head.appendChild(style);
    }
    style.textContent=`
      .homeResourcePhoto.one{
        background-image:linear-gradient(rgba(55,64,55,.08),rgba(55,64,55,.08)),url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&fm=jpg&q=80&w=900")!important;
        background-position:center 55%!important;
      }
      .homeResourcePhoto.two{
        background-image:linear-gradient(rgba(66,62,53,.08),rgba(66,62,53,.08)),url("https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&fm=jpg&q=80&w=900")!important;
        background-position:center!important;
      }
      .homeResourcePhoto.three{
        background-image:linear-gradient(rgba(71,66,56,.14),rgba(71,66,56,.14)),url("https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&fm=jpg&q=80&w=900")!important;
        background-position:center 58%!important;
      }
      .homeResourcePhoto.four{
        background-image:linear-gradient(rgba(67,72,65,.08),rgba(67,72,65,.08)),url("https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&fm=jpg&q=80&w=900")!important;
        background-position:center 55%!important;
      }
      .homeResourcePhoto.five{
        background-image:linear-gradient(rgba(136,105,66,.10),rgba(136,105,66,.10)),url("https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&fm=jpg&q=80&w=900")!important;
        background-position:center 50%!important;
        filter:none!important;
      }
      .homeTestimonialPhoto{
        background-image:url("https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&fm=jpg&q=78&w=600")!important;
        background-position:center!important;
      }
    `;
    document.querySelectorAll('.homeHeroImage').forEach(el=>{
      el.style.removeProperty('background-image');
      el.style.removeProperty('background-position');
      el.style.removeProperty('background-size');
      el.style.removeProperty('background-repeat');
    });
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',apply);
  else apply();
  new MutationObserver(()=>apply()).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('popstate',()=>setTimeout(apply,0));
})();
