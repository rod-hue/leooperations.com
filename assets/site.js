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
    document.addEventListener('click',function(e){var lv=e.target.closest('[data-video]');if(lv){e.preventDefault();fr.innerHTML='<video src="'+lv.dataset.video+'" controls autoplay playsinline></video>';yt.style.display='none';lb.classList.add('open');if(window.__lenis)__lenis.stop();return}var t=e.target.closest('[data-yt]');if(!t)return;e.preventDefault();yt.style.display='';
      fr.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+t.dataset.yt+'?autoplay=1&rel=0&playsinline=1" allow="autoplay; encrypted-media; fullscreen" allowfullscreen title="Leo Operations film"></iframe>';
      yt.href='https://www.youtube.com/watch?v='+t.dataset.yt;lb.classList.add('open');if(window.__lenis)__lenis.stop()});
    function close(){lb.classList.remove('open');setTimeout(function(){fr.innerHTML=''},400);if(window.__lenis)__lenis.start()}
    lb.querySelector('.lb-close').addEventListener('click',close);lb.addEventListener('click',function(e){if(e.target===lb)close()});addEventListener('keydown',function(e){if(e.key==='Escape')close()});
  }


  /* ---- resolution-aware video sources (4K on big screens) ---- */
  function q(v){var base=v.dataset.q;if(!base)return null;var px=innerWidth*Math.min(2,devicePixelRatio||1);return base+(px>=2300?'-4k':px>=1000?'-hd':'-sd')+'.mp4'}
  document.querySelectorAll('video[data-q]').forEach(function(v){v.dataset.src=q(v)});

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


  var mf=document.querySelector('.manifesto2 p');
  if(mf){(function sp(n){Array.from(n.childNodes).forEach(function(c){if(c.nodeType===3){var fr=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w))fr.appendChild(document.createTextNode(w));else{var s=document.createElement('span');s.className='w';s.textContent=w;fr.appendChild(s)}});n.replaceChild(fr,c)}else if(c.nodeType===1)sp(c)})})(mf)}

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


  /* ================= V2 cinematic ================= */
  var L2=document.getElementById('loader2');
  if(L2){var seen2=false;try{seen2=sessionStorage.getItem('leo_ld2')}catch(e){}
    if(seen2){L2.remove()}else{try{sessionStorage.setItem('leo_ld2','1')}catch(e){}
      if(window.__lenis)__lenis.stop();var o2={v:0},cn=L2.querySelector('.cnt');
      gsap.timeline({onComplete:function(){L2.remove();if(window.__lenis)__lenis.start()}})
        .to(L2.querySelectorAll('.mid span'),{y:0,stagger:.12,duration:.8,ease:'expo.out'},0)
        .to(o2,{v:100,duration:1.6,ease:'power2.inOut',onUpdate:function(){cn.textContent=Math.round(o2.v)}},0)
        .to(L2.querySelector('.bar'),{scaleX:1,duration:1.6,ease:'power2.inOut'},0)
        .to(L2,{clipPath:'inset(0 0 100% 0)',duration:.9,ease:'expo.inOut'},1.75)}}
  var d2=document.getElementById('loader2')?2.0:0.2;
  if(document.querySelector('.hero2')){
    gsap.fromTo('.hero2 .media video',{scale:1.18},{scale:1,duration:2.6,ease:'expo.out',delay:d2-.6});
    gsap.to('.hero2 .name .l>span',{y:0,duration:1.4,ease:'expo.out',stagger:.12,delay:d2});
    gsap.from('.hero2 .topline,.hero2 .foot,.badge2',{opacity:0,y:20,duration:1,delay:d2+.5});
    gsap.to('.hero2 .media',{yPercent:16,ease:'none',scrollTrigger:{trigger:'.hero2',start:'top top',end:'bottom top',scrub:true}});
    gsap.to('.hero2 .name .l:first-child>span',{xPercent:-10,ease:'none',scrollTrigger:{trigger:'.hero2',start:'top top',end:'bottom top',scrub:true}});
    gsap.to('.hero2 .name .l2>span',{xPercent:8,ease:'none',scrollTrigger:{trigger:'.hero2',start:'top top',end:'bottom top',scrub:true}});
    gsap.to('.hero2 .name,.hero2 .foot',{opacity:0,ease:'none',scrollTrigger:{trigger:'.hero2',start:'40% top',end:'90% top',scrub:true}});
  }
  if(document.querySelector('.manifesto2')) gsap.to('.manifesto2 .w',{opacity:1,stagger:.1,ease:'none',scrollTrigger:{trigger:'.manifesto2 p',start:'top 80%',end:'bottom 45%',scrub:true}});
  if(document.querySelector('.reel2')){var rv=document.querySelector('.reel2 .frame video');
    gsap.timeline({scrollTrigger:{trigger:'.reel2',start:'top top',end:'+=160%',pin:'.reel2 .pin',scrub:.8,onToggle:function(s){if(s.isActive){if(!rv.src)rv.src=rv.dataset.src;rv.play().catch(function(){})}}}})
      .to('.reel2 .frame',{clipPath:'inset(0% 0% 0% 0% round 0px)',ease:'power2.inOut',duration:1},0)
      .to('.reel2 .frame video',{scale:1,ease:'none',duration:1.3},0)
      .fromTo('.reel2 .word',{scale:.7,opacity:0},{scale:1.15,opacity:1,duration:1},0)
      .to('.reel2 .word',{opacity:0,duration:.3},1.1)
      .from('.reel2 .play',{opacity:0,y:30,duration:.3},1.05).to({}, {duration:.3});
  }
  var mm2=gsap.matchMedia();
  var rcs=gsap.utils.toArray('.rc2 .rc'),rdots=gsap.utils.toArray('.rc2 .dots i');
  function cu(el){var o={v:0};gsap.to(o,{v:+el.dataset.n,duration:1.6,ease:'power3.out',onUpdate:function(){el.textContent=Math.round(o.v).toLocaleString()}})}
  if(rcs.length){
    mm2.add('(min-width: 861px)',function(){gsap.set(rcs,{autoAlpha:0,y:60});gsap.set(rcs[0],{autoAlpha:1,y:0});var shown=rcs.map(function(){return false});
      function show(i){rdots.forEach(function(d,j){d.classList.toggle('on',j===i)});for(var k=0;k<=i;k++)if(!shown[k]){shown[k]=true;cu(rcs[k].querySelector('[data-n]'))}}
      var t=gsap.timeline({scrollTrigger:{trigger:'.rc2',start:'top top',end:'+='+(rcs.length*85)+'%',pin:'.rc2 .pin',scrub:.6,onUpdate:function(s){show(Math.min(rcs.length-1,Math.floor(s.progress*rcs.length*.999)))},onEnter:function(){show(0)}}});
      for(var i=1;i<rcs.length;i++)t.to(rcs[i-1],{autoAlpha:0,y:-60,duration:.5},i).to(rcs[i],{autoAlpha:1,y:0,duration:.5},i+.15);t.to({}, {duration:.6})});
    mm2.add('(max-width: 860px)',function(){rcs.forEach(function(c){ScrollTrigger.create({trigger:c,start:'top 82%',once:true,onEnter:function(){cu(c.querySelector('[data-n]'))}})})});
  }
  var sl=gsap.utils.toArray('.svc2 .slide');
  if(sl.length){var segs=gsap.utils.toArray('.svc2 .segs b'),cnt=document.querySelector('.svc2 .count'),cur=-1;
    function act(i){if(i===cur)return;cur=i;sl.forEach(function(s,j){var v=s.querySelector('video');if(Math.abs(j-i)<=1&&!v.src)v.src=v.dataset.src;if(j===i)v.play().catch(function(){});else v.pause()});if(cnt)cnt.textContent=String(i+1).padStart(2,'0')+' / '+String(sl.length).padStart(2,'0')}
    gsap.set(sl[0],{clipPath:'inset(0% 0% 0% 0%)'});gsap.set(sl.slice(1),{clipPath:'inset(100% 0% 0% 0%)'});
    var st=gsap.timeline({scrollTrigger:{trigger:'.svc2',start:'top top',end:'+='+(sl.length*100)+'%',pin:'.svc2 .stage',scrub:.7,anticipatePin:1,
      snap:{snapTo:function(v){if(window.__jumping)return v;var d=st.duration(),t=v*d,b=0;Object.values(st.labels).forEach(function(l){if(Math.abs(l-t)<Math.abs(b-t))b=l});return b/d},duration:{min:.2,max:.6},ease:'power2.inOut',delay:.08},
      onUpdate:function(){var t=st.time();act(Math.max(0,Math.min(sl.length-1,Math.floor(t+.45))));segs.forEach(function(b,j){b.style.transform='scaleX('+Math.max(0,Math.min(1,t-j+1))+')'})},
      onToggle:function(s){if(!s.isActive)sl.forEach(function(x){x.querySelector('video').pause()});else{cur=-1;act(Math.max(0,Math.min(sl.length-1,Math.floor(st.time()+.45))))}}}});
    st.addLabel('s0',0);
    sl.forEach(function(s,i){if(!i)return;var ti=s.querySelectorAll('h3 span'),ui=s.querySelectorAll('.meta,p,.btn');
      st.to(s,{clipPath:'inset(0% 0% 0% 0%)',ease:'power3.inOut',duration:1},i-1+.1).fromTo(s.querySelector('video'),{scale:1.3},{scale:1,ease:'power2.out',duration:1},i-1+.1)
        .to(sl[i-1].querySelector('.ui'),{y:-80,opacity:0,duration:.5},i-1+.1).fromTo(ti,{yPercent:110},{yPercent:0,stagger:.06,duration:.5,ease:'power3.out'},i-1+.55)
        .fromTo(ui,{opacity:0,y:20},{opacity:1,y:0,duration:.4},i-1+.7).addLabel('s'+i,i+.1)});
    st.to({}, {duration:.4});
  }
  mm2.add('(min-width: 861px)',function(){var tr=document.querySelector('.tl2 .track');if(!tr)return;var dist=function(){return tr.scrollWidth-innerWidth};
    var h=gsap.to(tr,{x:function(){return -dist()},ease:'none',scrollTrigger:{trigger:'.tl2',start:'top top',end:function(){return '+='+dist()},pin:'.tl2 .pin',scrub:.8,invalidateOnRefresh:true}});
    gsap.utils.toArray('.tl2 .card').forEach(function(c){gsap.from(c.querySelector('.yr'),{yPercent:60,opacity:0,ease:'power2.out',scrollTrigger:{trigger:c,containerAnimation:h,start:'left 95%',end:'left 60%',scrub:true}})})});
  gsap.from('.cta-circle',{scale:.4,opacity:0,duration:1.4,ease:'elastic.out(1,.6)',scrollTrigger:{trigger:'.cta2',start:'top 75%'}});

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

/* ===== V3: national layer ===== */
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches, G=window.gsap;
  /* image lightbox */
  var lb=document.getElementById('lb');
  if(lb){var fr=lb.querySelector('.lb-frame'),ya=lb.querySelector('a');
    document.addEventListener('click',function(e){var t=e.target.closest('[data-img]');
      if(!t||t.tagName==='LI'){if(e.target.closest('[data-video],[data-yt]'))fr.classList.remove('img');return}
      e.preventDefault();e.stopPropagation();fr.classList.add('img');fr.innerHTML='<img src="'+t.dataset.img+'" alt="">';if(ya)ya.style.display='none';lb.classList.add('open');if(window.__lenis)__lenis.stop()},true)}
  /* design wall filter */
  var chips=document.querySelectorAll('.wchips button');
  chips.forEach(function(b){b.addEventListener('click',function(){chips.forEach(function(x){x.classList.toggle('on',x===b)});var w=b.dataset.w;
    document.querySelectorAll('.wt').forEach(function(t){t.classList.toggle('hide',w!=='all'&&t.dataset.w!==w)});if(window.ScrollTrigger)ScrollTrigger.refresh()})});
  /* sector peek */
  var pk=document.querySelector('.sx-peek');
  if(pk&&matchMedia('(hover:hover)').matches){var pi=pk.querySelector('img'),tx=0,ty=0,cx=0,cy=0,raf;
    document.querySelectorAll('.sx li').forEach(function(li){li.addEventListener('mouseenter',function(){pi.src=li.dataset.img;pk.classList.add('on')});li.addEventListener('mouseleave',function(){pk.classList.remove('on')})});
    addEventListener('mousemove',function(e){tx=e.clientX+170;ty=e.clientY;if(!raf)raf=requestAnimationFrame(function loop(){cx+=(tx-cx)*.14;cy+=(ty-cy)*.14;pk.style.left=cx+'px';pk.style.top=cy+'px';raf=Math.abs(tx-cx)+Math.abs(ty-cy)>.5?requestAnimationFrame(loop):0})})}
  /* map */
  var map=document.querySelector('.map2');
  if(map){var sp=[].slice.call(map.querySelectorAll('.states path[data-o]')),li=[].slice.call(map.querySelectorAll('.st li')),mc=map.querySelector('.mc'),
      arcs=[].slice.call(map.querySelectorAll('.arc')),cities=[].slice.call(map.querySelectorAll('.city')),N=sp.length;
    arcs.forEach(function(a){var L=a.getTotalLength();a.style.strokeDasharray=L;a.style.strokeDashoffset=L;a.dataset.l=L});
    function setP(p){var n=Math.round(p*N);sp.forEach(function(s){s.classList.toggle('lit',+s.dataset.o<n)});li.forEach(function(l){l.classList.toggle('lit',+l.dataset.o<n)});mc.textContent=n;
      var q=Math.max(0,Math.min(1,(p-.15)/.85));arcs.forEach(function(a,i){var k=Math.max(0,Math.min(1,q*arcs.length-i*.55));a.style.strokeDashoffset=a.dataset.l*(1-k);cities[i].style.opacity=k>.9?1:0})}
    if(reduce||!G){setP(1)}else{setP(0);
      ScrollTrigger.matchMedia({'(min-width: 861px)':function(){ScrollTrigger.create({trigger:map,start:'top top',end:'+=170%',pin:map.querySelector('.pin'),scrub:.6,onUpdate:function(s){setP(s.progress)}})},
        '(max-width: 860px)':function(){var o={p:0};ScrollTrigger.create({trigger:map,start:'top 60%',once:true,onEnter:function(){G.to(o,{p:1,duration:3.2,ease:'power2.inOut',onUpdate:function(){setP(o.p)}})}})}})}}
  /* magazine page turns */
  var bk=document.querySelector('.book');
  if(bk){var lv=[].slice.call(bk.querySelectorAll('.leaf')),T=lv.length-1;
    function turn(p){var f=p*T;lv.forEach(function(l,i){var r=Math.max(0,Math.min(1,f-i));l.style.transform='rotateY('+(-180*r)+'deg)';l.style.zIndex=r>.5?100+i:lv.length-i;
      var bend=Math.sin(r*Math.PI);l.style.filter='brightness('+(1-bend*.25)+')'});
      bk.style.transform='translateX('+(-Math.min(1,f)*0)+'px)'}
    if(reduce||!G){turn(0)}else{turn(0);
      ScrollTrigger.create({trigger:'.mag2',start:'top top',end:'+='+(T*55)+'%',pin:'.mag2 .pin',scrub:.7,onUpdate:function(s){turn(s.progress)}});
      lv.forEach(function(l){l.querySelectorAll('img').forEach(function(im){im.loading='eager'})})}}
  if(window.ScrollTrigger){ScrollTrigger.sort();ScrollTrigger.refresh()}
})();
