from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TVector3
import math

Lumi = 0.22
ProtonsPerN = 74
Factor001 = 0.3678*Lumi*ProtonsPerN
Factor01 = 0.2651*Lumi*ProtonsPerN
Factor1 = 0.12*Lumi*ProtonsPerN

data=readLHEF('FFop3_cuts/30_1.lhe')
data1=readLHEF('FFop3_cuts/30_01.lhe')
data2=readLHEF('FFop3_cuts/30_001.lhe')

photons=data.getParticlesByIDs([22,-22])
electrons=data.getParticlesByIDs([11,-11])

photons1=data1.getParticlesByIDs([22,-22])
electrons1=data1.getParticlesByIDs([11,-11])

photons2=data2.getParticlesByIDs([22,-22])
electrons2=data2.getParticlesByIDs([11,-11])

c_mom=TCanvas()
hist_Pz_out_1=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| Min 1 GeV", 100,0,1)
hist_Pz_out_01=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| Min 0.1 GeV", 100,0,1)
hist_Pz_out_001=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| Min 0.01GeV", 100,0,1)

elec_vect = []
phot_vect = []

for e in electrons:
    e_out = TVector3()
    if e.status is 1:
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_vect.append(e_out)
for g in photons:
    g_out = TVector3()
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_vect.append(e_out)
for i,pe in enumerate(elec_vect):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect[i].Mag2())
    proj = elec_mom_vect[i].Cross(phot_mom_vect[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_Pz_out_1.Fill(value,Factor1)



elec_vect1 = []
phot_vect1 = []

for e in electrons1:
    e_out = TVector3()
    if e.status is 1:
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_vect1.append(e_out)
for g in photons1:
    g_out = TVector3()
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_vect1.append(e_out)
for i,pe in enumerate(elec_vect1):
    proj = TVector3()
    mag = math.sqrt(elec_vect1[i].Mag2())
    proj = elec_vect1[i].Cross(phot_vect1[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_Pz_out_01.Fill(value,Factor01)

elec_vect2 = []
phot_vect2 = []

for e in electrons2:
    e_out = TVector3()
    if e.status is 1:
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_vect2.append(e_out)
for g in photons2:
    g_out = TVector3()
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_vect2.append(e_out)
for i,pe in enumerate(elec_vect2):
    proj = TVector3()
    mag = math.sqrt(elec_vect2[i].Mag2())
    proj = elec_vect2[i].Cross(phot_vect2[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_Pz_out_001.Fill(value,Factor001)

c_mom.cd()
hist_Pz_out_01.SetLineColor(2)
hist_Pz_out_01.Draw("HIST")
hist_Pz_out_01.GetXaxis().SetTitle("|pe' x pg|/|pe'|")
hist_Pz_out_1.Draw("HISTSAME")
hist_Pz_out_1.GetXaxis().SetTitle("|pe' x pg|/|pe'|")
hist_Pz_out_001.SetLineColor(6)
hist_Pz_out_001.Draw("HISTSAME")
hist_Pz_out_001.GetXaxis().SetTitle("|pe' x pg|/|pe'|")
c_mom.SaveAs("transmom.root")
