import math
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


# Input Parameters
R = 25               # candle radius in mm
R_0 = 2              # burning rod diameter in mm
T = 2.5              # wax sheet thicknes in mm
Z_step = 1           # height output step in mm

# Do not change anything below this text unless you want to :-)

def pf(x):
  return(0.5*x*math.sqrt(1+x**2)+0.5*math.log(x+math.sqrt(1+x**2)))

# gets a radius as a function of phase angle
def get_r(phi):
  return(R_0+0.5*T+0.5/math.pi*T*phi)

# gets a strip length as a function of phase angle
def get_l(phi):
  shift = 2*math.pi/T*R_0+math.pi
  return(0.5*T/math.pi*(pf(shift + phi)-pf(shift)))

# gets a strip half-width as a function of phase angle
def get_z(phi):
  r = get_r(phi)
  return(math.sqrt(R**2-r**2))

result = [] 

phi = 0
dphi = 0.1*math.pi/180

next_z = R 

print("l,z,r")
while ((R**2-get_r(phi)**2) >= 0):
  l = get_l(phi)
  z = get_z(phi)
  if (z < next_z):
    print(math.floor(l), ',', z, ',', get_r(phi))
    if (phi > dphi):
      print((get_z(phi) - get_z(phi - dphi))/(get_l(phi) - get_l(phi - dphi)))
    result.append([math.floor(l), z])
    next_z -= Z_step
  phi += dphi

print(get_l(phi - dphi), ',', get_z(phi - dphi), ',', get_r(phi - dphi))
result.append([get_l(phi - dphi), get_z(phi - dphi)])

width, height = A4
margin = 15 * mm
vsep = 5 * mm
rel_x = margin
rel_y = margin + R * mm
pdf = canvas.Canvas("candle.pdf", pagesize=landscape(A4))
pdf.setLineWidth = 2
pdf.setStrokeColorRGB(0, 0, 0)

path_up = pdf.beginPath()
path_down = pdf.beginPath()

path_up.moveTo(rel_x, rel_y)
path_down.moveTo(rel_x, rel_y)
last_i = [0, 0]
for i in result:
  if ((i[0]*mm + rel_x) > (height - margin)):
    path_up.lineTo(last_i[0] * mm + rel_x, rel_y)
    path_down.lineTo(last_i[0] * mm + rel_x, rel_y)
    pdf.drawPath(path_up)
    pdf.drawPath(path_down)
    rel_x = margin - last_i[0]*mm
    if ((rel_y + 2*R*mm + vsep) > (width - margin)):
      pdf.showPage()
      rel_y = margin + R*mm
    else:  
      rel_y += (R+last_i[1])*mm + vsep
    path_up = pdf.beginPath()
    path_down = pdf.beginPath()
    path_up.moveTo(last_i[0] * mm + rel_x, rel_y)
    path_down.moveTo(last_i[0] * mm + rel_x, rel_y)
    path_up.lineTo(last_i[0] * mm + rel_x, last_i[1] * mm + rel_y)
    path_down.lineTo(last_i[0] * mm + rel_x, -last_i[1]*mm + rel_y)
  path_up.lineTo(i[0] * mm + rel_x, i[1] * mm + rel_y)
  path_down.lineTo(i[0] * mm + rel_x, -i[1]*mm + rel_y)
  last_i = i

pdf.drawPath(path_up)
pdf.drawPath(path_down)
pdf.save()
