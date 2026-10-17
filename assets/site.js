/* Leo Operations site motion engine */
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=matchMedia('(pointer:fine)').matches;

  /* ---- email (no address in source; built on interaction) ---- */
  function addr(el){return el.dataset.u+'@'+el.dataset.d}
  var shown=false;
  function reveal(){if(shown)return;shown=true;document.querySelectorAll('.em[data-u]').forEach(function(s){s.textContent=addr(s)})}
  ['pointerdown','touchstart','keydown','wheel'].forEach(function(e){addEventListener(e,reveal,{once:true,passive:true})});
  document.addEventListener('click',function(e){var a=e.target.closest('a[data-u]');if(!a)return;e.preventDefault();reveal();location.href='mai'+'lto:'+addr(a)+(a.dataset.s?'?subject='+a.dataset.s:'')});


  /* ---- face-aware cropping: recompute on every size so no face is ever cut ---- */
  function fit(el){var f=el.dataset.fx;if(!f)return;f=f.split(',').map(Number);var nw=el.naturalWidth||el.videoWidth||+el.getAttribute('width'),nh=el.naturalHeight||el.videoHeight||+el.getAttribute('height');
    if(el.tagName==='VIDEO'&&(!nw||!nh)){var pv=el.closest('.film');var pi=pv&&pv.querySelector('img');if(pi){nw=pi.naturalWidth||+pi.getAttribute('width');nh=pi.naturalHeight||+pi.getAttribute('height')}}
    var w=el.clientWidth,h=el.clientHeight;if(!nw||!nh||!w||!h)return;var sc=Math.max(w/nw,h/nh),rw=nw*sc,rh=nh*sc;
    function axis(a1,a2,b1,b2,R,V,bias){var box=(a2-a1)*R<=V*0.94?[a1,a2]:[b1,b2];var c=(box[0]+box[1])/2*R;var off=Math.min(0,Math.max(V-R,V*bias-c));return R>V+0.5?off/(V-R)*100:50}
    var fitsX=(f[2]-f[0])*rw<=w*0.94,fitsY=(f[3]-f[1])*rh<=h*0.94;
    if(el.tagName==='IMG'&&(!fitsX||!fitsY)){ if(!el.classList.contains('whole')){el.classList.add('whole');var bf=el.cloneNode();bf.removeAttribute('data-fx');bf.className='blurfill';bf.alt='';bf.setAttribute('aria-hidden','true');el.parentNode.insertBefore(bf,el)} return }
    if(el.classList.contains('whole')){el.classList.remove('whole');var ob=el.parentNode.querySelector('.blurfill');if(ob)ob.remove()}
    var px=axis(f[0],f[2],f[4],f[6],rw,w,.5),py=axis(f[1],f[3],f[5],f[7],rh,h,.42);
    el.style.objectPosition=px.toFixed(1)+'% '+py.toFixed(1)+'%';el.style.transformOrigin=el.style.objectPosition}
  function fitAll(){document.querySelectorAll('[data-fx]').forEach(fit)}
  document.querySelectorAll('img[data-fx]').forEach(function(i){if(!i.complete)i.addEventListener('load',function(){fit(i)})});
  fitAll();addEventListener('resize',function(){clearTimeout(window.__ft);window.__ft=setTimeout(fitAll,120)});addEventListener('load',fitAll);
  if('ResizeObserver' in window){var ro=new ResizeObserver(function(es){es.forEach(function(e){fit(e.target)})});document.querySelectorAll('[data-fx]').forEach(function(e){ro.observe(e)})}

  /* ---- mobile menu ---- */
  var bg=document.querySelector('.burger');
  if(bg)bg.addEventListener('click',function(){document.documentElement.classList.toggle('menu-open')});
  document.querySelectorAll('.mmenu a').forEach(function(a){a.addEventListener('click',function(){document.documentElement.classList.remove('menu-open')})});

  /* ---- lightbox ---- */
  var lb=document.getElementById('lb');
  if(lb){var fr=lb.querySelector('.lb-frame'),yt=lb.querySelector('a');
    document.addEventListener('click',function(e){var t=e.target.closest('[data-yt]');if(!t)return;e.preventDefault();
      fr.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+t.dataset.yt+'?autoplay=1&rel=0&playsinline=1" allow="autoplay; encrypted-media; fullscreen" allowfullscreen title="Leo Operations film"></iframe>';
      yt.href='https://www.youtube.com/watch?v='+t.dataset.yt;lb.classList.add('open');if(window.__lenis)__lenis.stop()});
    function close(){lb.classList.remove('open');setTimeout(function(){fr.innerHTML=''},400);if(window.__lenis)__lenis.start()}
    lb.querySelector('.lb-close').addEventListener('click',close);lb.addEventListener('click',function(e){if(e.target===lb)close()});addEventListener('keydown',function(e){if(e.key==='Escape')close()});
  }

  /* ---- videos: play only while visible ---- */
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){var v=en.target;
      if(en.isIntersecting){if(!v.src&&v.dataset.src)v.src=v.dataset.src;v.play().catch(function(){})}else v.pause()})},{rootMargin:'200px 0px',threshold:.01});
    document.querySelectorAll('video[data-src],video[autoplay]').forEach(function(v){io.observe(v)});
  }

  /* ---- filters (clients page) ---- */
  document.querySelectorAll('.filters button').forEach(function(b){b.addEventListener('click',function(){
    document.querySelectorAll('.filters button').forEach(function(x){x.classList.toggle('on',x===b)});
    var f=b.dataset.f;document.querySelectorAll('.client[data-cat]').forEach(function(c){c.style.display=(f==='all'||c.dataset.cat===f)?'':'none'});
    if(window.ScrollTrigger)ScrollTrigger.refresh();
  })});

  /* ---- living particle field ---- */
  var cv=document.getElementById('bgfx');
  if(cv&&!reduce){var cx=cv.getContext('2d'),W,H,P=[],dpr=Math.min(2,devicePixelRatio||1),mx=-999,my=-999;
    function rs(){W=cv.width=innerWidth*dpr;H=cv.height=innerHeight*dpr;cv.style.width=innerWidth+'px';cv.style.height=innerHeight+'px';
      var n=Math.round(Math.min(110,innerWidth*innerHeight/14000));P=[];for(var i=0;i<n;i++)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.25*dpr,vy:(Math.random()-.5)*.25*dpr,r:(Math.random()*1.6+.4)*dpr})}
    rs();addEventListener('resize',rs);addEventListener('mousemove',function(e){mx=e.clientX*dpr;my=e.clientY*dpr});
    (function loop(){cx.clearRect(0,0,W,H);
      for(var i=0;i<P.length;i++){var p=P[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;
        var dx=p.x-mx,dy=p.y-my,dd=dx*dx+dy*dy;if(dd<22000*dpr){p.x+=dx*.012;p.y+=dy*.012}
        cx.beginPath();cx.arc(p.x,p.y,p.r,0,6.28);cx.fillStyle='rgba(120,190,255,.55)';cx.fill();
        for(var j=i+1;j<P.length;j++){var q=P[j],ax=p.x-q.x,ay=p.y-q.y,d=ax*ax+ay*ay,L=(130*dpr)*(130*dpr);
          if(d<L){cx.strokeStyle='rgba(79,160,255,'+(.16*(1-d/L))+')';cx.lineWidth=dpr*.6;cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(q.x,q.y);cx.stroke()}}}
      requestAnimationFrame(loop)})();
  }

  if(!window.gsap){document.documentElement.classList.add('nogsap');var L0=document.getElementById('loader');if(L0)L0.remove();return}
  gsap.registerPlugin(ScrollTrigger);

  /* ---- smooth scroll ---- */
  if(!reduce&&window.Lenis){var lenis=new Lenis({lerp:.09});window.__lenis=lenis;lenis.on('scroll',ScrollTrigger.update);gsap.ticker.add(function(t){lenis.raf(t*1000)});gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length>1&&!a.dataset.u){var el=document.querySelector(id);if(el){e.preventDefault();lenis.scrollTo(el,{offset:-80,duration:1.4})}}})})}

  /* ---- loader ---- */
  var ld=document.getElementById('loader');
  if(ld){var seen=false;try{seen=sessionStorage.getItem('leo_ld')}catch(e){}
    if(seen||reduce){ld.remove()}else{try{sessionStorage.setItem('leo_ld','1')}catch(e){}
      gsap.timeline({onComplete:function(){ld.remove()}})
        .to(ld.querySelector('img'),{opacity:1,scale:1,duration:.9,ease:'expo.out'})
        .to(ld.querySelector('.ld-bar i'),{scaleX:1,duration:1,ease:'power2.inOut'},0.1)
        .to(ld,{clipPath:'inset(0 0 100% 0)',duration:.8,ease:'expo.inOut'},1.2)}}

  /* ---- progress + nav ---- */
  gsap.to('.progress',{scaleX:1,ease:'none',scrollTrigger:{start:0,end:'max',scrub:.3}});
  var nav=document.querySelector('.nav');ScrollTrigger.create({start:60,onToggle:function(s){nav.classList.toggle('scrolled',s.isActive)}});

  if(reduce){document.querySelectorAll('[data-count]').forEach(function(e){e.textContent=e.dataset.count+(e.dataset.suf||'')});return}

  /* ---- cursor + glow + magnetic ---- */
  if(fine){var c=document.querySelector('.cur'),gl=document.querySelector('.glow-cursor'),ci=c.querySelector('i');
    var xr=gsap.quickTo(ci,'x',{duration:.4,ease:'power3'}),yr=gsap.quickTo(ci,'y',{duration:.4,ease:'power3'}),xd=gsap.quickTo(c.querySelector('b'),'x',{duration:.08}),yd=gsap.quickTo(c.querySelector('b'),'y',{duration:.08});
    var gx=gsap.quickTo(gl,'x',{duration:1.2,ease:'power3'}),gy=gsap.quickTo(gl,'y',{duration:1.2,ease:'power3'});
    addEventListener('mousemove',function(e){xr(e.clientX);yr(e.clientY);xd(e.clientX);yd(e.clientY);gx(e.clientX);gy(e.clientY);
      var t=e.target.closest('[data-c]');if(t){c.classList.add('big');ci.setAttribute('data-l',t.dataset.c)}else c.classList.remove('big')});
    gsap.utils.toArray('.btn,.cta-pill').forEach(function(b){var mx=gsap.quickTo(b,'x',{duration:.5,ease:'elastic.out(1,.4)'}),my=gsap.quickTo(b,'y',{duration:.5,ease:'elastic.out(1,.4)'});
      b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();mx((e.clientX-r.left-r.width/2)*.3);my((e.clientY-r.top-r.height/2)*.4)});b.addEventListener('mouseleave',function(){mx(0);my(0)})});
    // 3D tilt on cards
    gsap.utils.toArray('.svc,.browser,.member,.win.big').forEach(function(card){
      card.addEventListener('mousemove',function(e){var r=card.getBoundingClientRect(),px=(e.clientX-r.left)/r.width-.5,py=(e.clientY-r.top)/r.height-.5;gsap.to(card,{rotateY:px*8,rotateX:-py*8,transformPerspective:900,duration:.6,ease:'power3'})});
      card.addEventListener('mouseleave',function(){gsap.to(card,{rotateY:0,rotateX:0,duration:.8,ease:'elastic.out(1,.5)'})})});
  }

  /* ---- hero intro ---- */
  var delay=document.getElementById('loader')?1.7:0.1;
  gsap.from('.hero .split-line>span',{yPercent:110,duration:1.3,ease:'expo.out',stagger:.1,delay:delay});
  gsap.from('.hero .eyebrow,.hero .lead,.hero-ctas',{y:30,opacity:0,duration:1,ease:'power3.out',stagger:.1,delay:delay+.4});
  gsap.fromTo('.hero-media video,.hero-media img',{scale:1.15},{scale:1,duration:2.4,ease:'expo.out',delay:delay-.4});
  gsap.to('.hero-media',{yPercent:18,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  gsap.to('.hero-inner',{yPercent:-20,opacity:0,ease:'none',scrollTrigger:{trigger:'.hero',start:'40% top',end:'bottom top',scrub:true}});

  /* ---- generic reveals ---- */
  gsap.utils.toArray('[data-r]').forEach(function(el){
    gsap.from(el,{y:60,opacity:0,duration:1.1,ease:'power3.out',delay:(+el.dataset.r||0)*.08,scrollTrigger:{trigger:el,start:'top 90%'}})});
  gsap.utils.toArray('.sec .split-line>span').forEach(function(s){
    gsap.from(s,{yPercent:110,duration:1.1,ease:'expo.out',scrollTrigger:{trigger:s,start:'top 92%'}})});

  /* ---- counters ---- */
  gsap.utils.toArray('[data-count]').forEach(function(el){var o={v:0},to=+el.dataset.count,suf=el.dataset.suf||'';
    ScrollTrigger.create({trigger:el,start:'top 88%',once:true,onEnter:function(){var st=el.closest('.stat');if(st)st.classList.add('in');
      gsap.to(o,{v:to,duration:2,ease:'power3.out',onUpdate:function(){el.textContent=Math.round(o.v).toLocaleString()+suf}})}})});

  /* ---- marquee velocity skew ---- */
  var sk=gsap.quickTo('.marq .t','skewX',{duration:.4,ease:'power3'});
  ScrollTrigger.create({onUpdate:function(s){sk(gsap.utils.clamp(-10,10,s.getVelocity()/-260))}});

  /* ---- websites: horizontal pinned scroll ---- */
  var mm=gsap.matchMedia();
  mm.add('(min-width: 861px)',function(){var tr=document.querySelector('.sites-track');if(!tr)return;
    var dist=function(){return tr.scrollWidth-innerWidth};
    gsap.to(tr,{x:function(){return -dist()},ease:'none',scrollTrigger:{trigger:'.sites',start:'top top',end:function(){return '+='+dist()},pin:'.sites-pin',scrub:.8,invalidateOnRefresh:true}});
  });

  /* ---- parallax media ---- */
  gsap.utils.toArray('[data-par]').forEach(function(el){gsap.fromTo(el,{yPercent:-8},{yPercent:8,ease:'none',scrollTrigger:{trigger:el.parentElement,start:'top bottom',end:'bottom top',scrub:true}})});

  addEventListener('load',function(){ScrollTrigger.refresh()});
})();
