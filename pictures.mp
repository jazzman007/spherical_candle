beginfig(1);
  path wick;
  wick = fullcircle scaled 20;
  fill wick withcolor black;

  path wax;
  wax = (10,0)..(0,15)..(-20,0)..(0,-25)..(30,0)..(0,35)..(-40,0)--(-60,0)..(0,55)..(50,0)..(0,-45)..(-40,0)..(0,35)..(30,0)--cycle;
  fill wax withcolor 0.9*white;
  draw wax;

  draw (20,0)..(0,25)..(-30,0)..(0,-35)..(40,0)..(0,45)..(-50,0) dashed evenly;

  drawarrow (-70,0)--(70,0);
  drawarrow (0,-70)--(0,70);
  label.bot (btex $x$ etex, (70,0));
  label.lft (btex $y$ etex, (0,70));

endfig;

beginfig(2);
  path wick;
  wick = (-10,-60)--(10,-60)--(10,60)--(-10,60)--cycle;
  fill wick withcolor black;

  fill wick yscaled 0.9 shifted (20,0) withcolor 0.9*white; 
  draw wick yscaled 0.9 shifted (20,0); 
  fill wick yscaled 0.9 shifted (-20,0) withcolor 0.9*white; 
  draw wick yscaled 0.9 shifted (-20,0); 
  fill wick yscaled 0.8 shifted (40,0) withcolor 0.9*white; 
  draw wick yscaled 0.8 shifted (40,0); 
  fill wick yscaled 0.8 shifted (-40,0) withcolor 0.9*white; 
  draw wick yscaled 0.8 shifted (-40,0); 

  path midsurface;
  midsurface = (0,-60)--(0,60);
  draw midsurface yscaled 0.9 shifted (20,0) dashed evenly;
  draw midsurface yscaled 0.9 shifted (-20,0) dashed evenly;
  draw midsurface yscaled 0.8 shifted (40,0) dashed evenly;
  draw midsurface yscaled 0.8 shifted (-40,0) dashed evenly;

  drawarrow (-70,0)--(70,0);
  drawarrow (0,-70)--(0,70);
  label.bot (btex $r$ etex, (70,0));
  label.lft (btex $z$ etex, (0,70));
endfig;

\beginfig(3);
  path template;
  template = (150,0)--(0,10)--(0,-10)--cycle;
  fill template withcolor 0.9*white;
  draw template;

  drawarrow (0,0)--(160,0);
  drawarrow (0,0)--(0,20);
  label.bot (btex $l$ etex, (160,0));
  label.lft (btex $z$ etex, (0,20));
\endfig;
