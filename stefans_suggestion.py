from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TVector3
import math

data0=[]
data1=[]
data2=[]
data3=[]
data4 =[]

Lumi = 0.22
ProtonsPerN = 74
Factor5  = 6.063*Lumi*ProtonsPerN
Factor30 = 0.1795*Lumi*ProtonsPerN
Factor20 = 0.4495*Lumi*ProtonsPerN
Factor10 = 1.851*Lumi*ProtonsPerN
Factor15 = 0.8324*Lumi*ProtonsPerN
Factor25 = 0.2666*Lumi*ProtonsPerN
FF=3
if FF==1:
    Eventweight =278.4
    data1=readLHEF('FFop1_cuts/30deg.lhe')
if FF == 2:
    Eventweight= 0.0002478
    data1=readLHEF('FFop2_cuts/30deg.lhe')
if FF==3:
    Eventweight = 0.3678
    data1=readLHEF('FFop3_cuts/30_1.lhe')
    data2=readLHEF('FFop3_cuts/20deg_1.lhe')
    data3=readLHEF('FFop3_cuts/10deg_1.lhe')
if FF==4:
    Eventweight = 0.003193
    data1=readLHEF('FFop4_cuts/30deg.lhe')

print("FF is :",FF)

electrons1=data1.getParticlesByIDs([11,-11])
electrons2=data2.getParticlesByIDs([11,-11])
electrons3=data3.getParticlesByIDs([11,-11])

photons1=data1.getParticlesByIDs([22,-22])
photons2=data2.getParticlesByIDs([22,-22])
photons3=data3.getParticlesByIDs([22,-22])


c_mom=TCanvas()
c_mom.Divide(2,2)

hist_X_10=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| #theta_{#gamma} > 10", 100,0,1)
hist_X_20=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| #theta_{#gamma} > 20", 100,0,1)
hist_X_30=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| #theta_{#gamma} > 30", 100,0,1)

elec_mom_vect10 = []
phot_mom_vect10 = []
elec_r_vect10 = []
phot_r_vect10 = []
elec_pt_vect10 = []
phot_pt_vect10 = []

for e in electrons3:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect10.append(e_out)
        elec_r_vect10.append(r*math.cos(e.pz/r))
for g in photons3:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect10.append(g_out)
    phot_r_vect10.append(r*math.cos(g.pz/r))

for i,pe in enumerate(elec_mom_vect10):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect10[i].Mag2())
    proj = elec_mom_vect10[i].Cross(phot_mom_vect10[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_X_10.Fill(value,Factor10)

elec_mom_vect20 = []
phot_mom_vect20 = []
elec_r_vect20 = []
phot_r_vect20 = []
elec_pt_vect20 = []
phot_pt_vect20 = []

for e in electrons2:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect20.append(e_out)
        elec_r_vect20.append(r*math.cos(e.pz/r))
for g in photons2:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect20.append(g_out)
    phot_r_vect20.append(r*math.cos(g.pz/r))

for i,pe in enumerate(elec_mom_vect20):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect20[i].Mag2())
    proj = elec_mom_vect20[i].Cross(phot_mom_vect20[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_X_20.Fill(value,Factor20)

elec_mom_vect30 = []
phot_mom_vect30 = []
elec_r_vect30 = []
phot_r_vect30 = []
elec_pt_vect30 = []
phot_pt_vect30 = []

for e in electrons1:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect30.append(e_out)
        elec_r_vect30.append(r*math.cos(e.pz/r))
for g in photons1:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect30.append(g_out)
    phot_r_vect30.append(r*math.cos(g.pz/r))

for i,pe in enumerate(elec_mom_vect30):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect30[i].Mag2())
    proj = elec_mom_vect30[i].Cross(phot_mom_vect30[i])
    print(math.sqrt(proj.Mag2()))
    value = math.sqrt(proj.Mag2())/mag
    hist_X_30.Fill(value,Factor30)

c_mom.cd(1)
hist_X_10.GetXaxis().SetTitle("|pe' x pg|/|pe'|  ")
hist_X_10.Draw("HISTSAME")
hist_X_20.GetXaxis().SetTitle("|pe' x pg|/|pe'| ")
hist_X_20.SetLineColor(2)
hist_X_20.Draw("HISTSAME")
hist_X_30.GetXaxis().SetTitle("|pe' x pg|/|pe'| ")
hist_X_30.SetLineColor(6)
hist_X_30.Draw("HISTSAME")

c_mom.SaveAs("dr_stefan.root")
