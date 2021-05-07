from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TVector3
import math

data0=[]
data1=[]
data2=[]

Lumi = 0.22
ProtonsPerN = 74
Factor001 = 0.3678*Lumi*ProtonsPerN
Factor01 = 0.2651*Lumi*ProtonsPerN
Factor1 = 0.12*Lumi*ProtonsPerN
FF=3
if FF==1:
    Eventweight =278.4
    data1=readLHEF('FFop1_cuts/30deg.lhe')
if FF == 2:
    Eventweight= 0.0002478
    data1=readLHEF('FFop2_cuts/30deg.lhe')
if FF==3:
    Eventweight = 0.3678
    data0=readLHEF('FFop3_cuts/30_001.lhe')
    data1=readLHEF('FFop3_cuts/30_01.lhe')
    data2=readLHEF('FFop3_cuts/30_1.lhe')

if FF==4:
    Eventweight = 0.003193
    data1=readLHEF('FFop4_cuts/30deg.lhe')

print("FF is :",FF)
electrons0=data2.getParticlesByIDs([11,-11])
electrons1=data1.getParticlesByIDs([11,-11])
electrons2=data0.getParticlesByIDs([11,-11])

photons0=data2.getParticlesByIDs([22,-22])
photons1=data1.getParticlesByIDs([22,-22])
photons2=data0.getParticlesByIDs([22,-22])

proton0=data0.getParticlesByIDs([9000002,-9000002])
proton1=data1.getParticlesByIDs([9000002,-9000002])
proton2=data2.getParticlesByIDs([9000002,-9000002])

c_mom=TCanvas()
c_mom.Divide(2,2)

hist_X_1=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| P_{#gamma}^{min} > 1 GeV", 100,0,1)
hist_X_01=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| P_{#gamma}^{min} > 0.1 GeV", 100,0,1)
hist_X_001=TH1F("|pe' x pg|/|pe'| ", "|pe' x pg|/|pe'| P_{#gamma}^{min} > 0.01 GeV", 100,0,1)

hist_dr_1=TH1F("Opening Angle ", "Opening Angle P_{#gamma}^{min} > 1 GeV", 100,0,2)
hist_dr_01=TH1F("Opening Angle", "Opening Angle P_{#gamma}^{min} > 0.1 GeV", 100,0,2)
hist_dr_001=TH1F("Opening Angle", "Opening Angle P_{#gamma}^{min} > 0.01 GeV", 100,0,2)

hist_pt_1_elec=TH1F("pt ", "pt P_{#gamma}^{min} > 1 GeV", 100,0,1.5)
hist_pt_01_elec=TH1F("pt ", "pt P_{#gamma}^{min} > 0.1 GeV", 100,0,1.5)
hist_pt_001_elec=TH1F("pt ", "pt P_{#gamma}^{min} > 0.01 GeV", 100,0,1.5)

hist_pt_1_pro=TH1F("pt ", "pt P_{#gamma}^{min} > 1 GeV", 100,0,1.5)
hist_pt_01_pro=TH1F("pt ", "pt P_{#gamma}^{min} > 0.1 GeV", 100,0,1.5)
hist_pt_001_pro=TH1F("pt ", "pt P_{#gamma}^{min} > 0.01 GeV", 100,0,1.5)

hist_pt_1_phot=TH1F("pt ", "pt P_{#gamma}^{min} > 1 GeV", 100,0,1.5)
hist_pt_01_phot=TH1F("pt ", "pt P_{#gamma}^{min} > 0.1 GeV", 100,0,1.5)
hist_pt_001_phot=TH1F("pt ", "pt P_{#gamma}^{min} > 0.01 GeV", 100,0,1.5)

elec_mom_vect10 = []
phot_mom_vect10 = []
elec_r_vect10 = []
phot_r_vect10 = []
elec_pt_vect10 = []
phot_pt_vect10 = []

for e in electrons0:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect10.append(e_out)
        elec_r_vect10.append(r*math.cos(e.pz/r))
        hist_pt_1_elec.Fill(e.pt,Factor1)
for g in photons0:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect10.append(g_out)
    phot_r_vect10.append(r*math.cos(g.pz/r))
    hist_pt_1_phot.Fill(g.pt, Factor1)
for p in proton0:
    if p.status is 1:
        hist_pt_1_pro.Fill(p.pt, Factor1)
for i,pe in enumerate(elec_mom_vect10):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect10[i].Mag2())
    proj = elec_mom_vect10[i].Cross(phot_mom_vect10[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_X_1.Fill(value,Factor1)
for i,pe in enumerate(elec_r_vect10):
    proj = TVector3()
    magE = math.sqrt(elec_mom_vect10[i].Mag2())
    magG = math.sqrt(phot_mom_vect10[i].Mag2())
    proj = elec_mom_vect10[i].Cross(phot_mom_vect10[i])
    value = math.asin(math.sqrt(proj.Mag2())/(magE*magG))
    hist_dr_1.Fill(value,Factor1)

elec_mom_vect20 = []
phot_mom_vect20 = []
elec_r_vect20 = []
phot_r_vect20 = []
elec_pt_vect20 = []
phot_pt_vect20 = []

for e in electrons1:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect20.append(e_out)
        elec_r_vect20.append(r*math.cos(e.pz/r))
        hist_pt_01_elec.Fill(e.pt,Factor01)
for g in photons1:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect20.append(g_out)
    phot_r_vect20.append(r*math.cos(g.pz/r))
    hist_pt_01_phot.Fill(g.pt,Factor01)
for p in proton1:
    if p.status is 1:
        hist_pt_01_pro.Fill(p.pt, Factor01)
for i,pe in enumerate(elec_mom_vect20):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect20[i].Mag2())
    proj = elec_mom_vect20[i].Cross(phot_mom_vect20[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_X_01.Fill(value,Factor01)
for i,pe in enumerate(elec_r_vect20):
    proj = TVector3()
    magE = math.sqrt(elec_mom_vect20[i].Mag2())
    magG = math.sqrt(phot_mom_vect20[i].Mag2())
    proj = elec_mom_vect20[i].Cross(phot_mom_vect20[i])
    value = math.asin(math.sqrt(proj.Mag2())/(magE*magG))
    hist_dr_01.Fill(value,Factor01)

elec_mom_vect30 = []
phot_mom_vect30 = []
elec_r_vect30 = []
phot_r_vect30 = []
elec_pt_vect30 = []
phot_pt_vect30 = []

for e in electrons2:
    e_out = TVector3()
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        e_out.SetXYZ(e.px,e.py,e.pz)
        elec_mom_vect30.append(e_out)
        elec_r_vect30.append(r*math.cos(e.pz/r))
        hist_pt_001_elec.Fill(e.pt,Factor001)
for g in photons2:
    g_out = TVector3()
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    g_out.SetXYZ(g.px,g.py,g.pz)
    phot_mom_vect30.append(g_out)
    phot_r_vect30.append(r*math.cos(g.pz/r))
    hist_pt_001_phot.Fill(g.pt,Factor001)
for p in proton2:
    if p.status is 1:
        hist_pt_001_pro.Fill(p.pt, Factor001)
for i,pe in enumerate(elec_mom_vect30):
    proj = TVector3()
    mag = math.sqrt(elec_mom_vect30[i].Mag2())
    proj = elec_mom_vect30[i].Cross(phot_mom_vect30[i])
    value = math.sqrt(proj.Mag2())/mag
    hist_X_001.Fill(value,Factor001)
for i,pe in enumerate(elec_r_vect30):
    proj = TVector3()
    magE = math.sqrt(elec_mom_vect30[i].Mag2())
    magG = math.sqrt(phot_mom_vect30[i].Mag2())
    proj = elec_mom_vect30[i].Cross(phot_mom_vect30[i])
    value = math.asin(math.sqrt(proj.Mag2())/(magE*magG))
    hist_dr_001.Fill(value,Factor001)

c_mom.cd(1)
hist_dr_001.GetXaxis().SetTitle("Opening Angle [rad]")
hist_dr_001.Draw("HIST")
hist_dr_01.GetXaxis().SetTitle("Opening Angle [rad]")
hist_dr_01.SetLineColor(3)
hist_dr_01.Draw("HISTSAME")
hist_dr_1.SetLineColor(2)
hist_dr_1.GetXaxis().SetTitle("Opening Angle [rad]")
hist_dr_1.Draw("HISTSAME")
c_mom.cd(2)
hist_pt_001_pro.GetXaxis().SetTitle("outgoing proton p_{t} [ GeV/c]")
hist_pt_001_pro.Draw("HIST")
hist_pt_1_pro.GetXaxis().SetTitle("outgoing proton p_{t} [ GeV/c]")
hist_pt_1_pro.SetLineColor(2)
hist_pt_1_pro.Draw("HISTSAME")
hist_pt_01_pro.GetXaxis().SetTitle("outgoing proton p_{t} [ GeV/c]")
hist_pt_01_pro.SetLineColor(3)
hist_pt_01_pro.Draw("HISTSAME")

c_mom.cd(3)
hist_pt_001_phot.GetXaxis().SetTitle("photon p_{t} [ GeV/c]")
hist_pt_001_phot.Draw("HIST")
hist_pt_1_phot.GetXaxis().SetTitle("photon p_{t} [ GeV/c]")
hist_pt_1_phot.SetLineColor(2)
hist_pt_1_phot.Draw("HISTSAME")
hist_pt_01_phot.GetXaxis().SetTitle("photon p_{t} [ GeV/c]")
hist_pt_01_phot.SetLineColor(3)
hist_pt_01_phot.Draw("HISTSAME")


c_mom.cd(4)
hist_pt_001_elec.GetXaxis().SetTitle("outgoing electron p_{t} [ MeV/c]")
hist_pt_001_elec.Draw("HIST")
hist_pt_1_elec.GetXaxis().SetTitle("outgoing electron p_{t} [ MeV/c]")
hist_pt_1_elec.SetLineColor(2)
hist_pt_1_elec.Draw("HISTSAME")
hist_pt_01_elec.GetXaxis().SetTitle("outgoing electron p_{t} [ MeV/c]")
hist_pt_01_elec.SetLineColor(3)
hist_pt_01_elec.Draw("HISTSAME")


c_mom.SaveAs("dr_photon_e_cut.root")
