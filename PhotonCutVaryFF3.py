from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector, TF1
import math
data0=[]
data1=[]
data2=[]

EventWeight = 0.3678
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

print("FF is :",FF," Event Weight is : ", EventWeight)
electrons0=data0.getParticlesByIDs([11,-11])
electrons1=data1.getParticlesByIDs([11,-11])
electrons2=data2.getParticlesByIDs([11,-11])

c=TCanvas()
c.Divide(2,2)
c_mom=TCanvas()
c_mom.Divide(2,2)
clab=TCanvas()
clab.Divide(2,2)

hist_e_theta_out=TH1F("theta_elec_out", "Outgoing Electron Theta",100,0, math.pi)
hist_e_phi_out=TH1F("phi_elec_out", "Outgoing Electron Phi",100,-math.pi,math.pi)
hist_4in=TH1F("q^{2} in", "Incoming Electron q^{2} ", 100,0,0.00001)
hist_4out=TH1F("q^{2} out", "Outgoing Electron q^{2} ", 100,0,0.00001)

hist_Px_out_001=TH1F("P_{z} out 5 deg", "P_{lab}^{#gamma} = 0.01GeV ", 100,-2,2)
hist_Pz_out_001=TH1F("P_{x} out 5 deg", "P_{lab}^{#gamma} = 0.01GeV ", 100,-2,2)
hist_Py_out_001=TH1F("P_{y} out 5 deg", "P_{lab}^{#gamma} = 0.01GeV  ", 100,-2,2)
hist_E_out_001=TH1F("E out 5 deg", "P_{lab}^{#gamma} = 0.01GeV ", 100,0,2)

hist_Px_out_01=TH1F("P_{z} out 20 deg", "P_{lab}^{#gamma} = 0.1GeV ", 100,-2,2)
hist_Pz_out_01=TH1F("P_{x} out 20 deg", "P_{lab}^{#gamma} = 0.1GeV ", 100,-2,2)
hist_Py_out_01=TH1F("P_{y} out 20 deg", "P_{lab}^{#gamma} = 0.1GeV ", 100,-2,2)
hist_E_out_01=TH1F("E out  20 deg", "P_{lab}^{#gamma} = 0.01GeV ", 100,0,2)

hist_Px_out_1=TH1F("P_{z} out 30 deg", "P_{lab}^{#gamma} = 1GeV ", 100,-2,2)
hist_Pz_out_1=TH1F("P_{x} out 30 deg", "P_{lab}^{#gamma} = 1GeV ", 100,-2,2)
hist_Py_out_1=TH1F("P_{y} out 30 deg", "P_{lab}^{#gamma} = 1GeV ", 100,-2,2)
hist_E_out_1=TH1F("E out 30 deg", "P_{lab}^{#gamma} = 1GeV ", 100,0,2)

for e in electrons0:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor001))
        hist_e_theta_out.Fill(theta,(Factor001))
        hist_4out.Fill(squared_4mom,(Factor001))
        hist_Px_out_001.Fill(e.px,(Factor001))
        hist_Py_out_001.Fill(e.py,(Factor001))
        hist_Pz_out_001.Fill(e.pz,(Factor001))
        hist_E_out_001.Fill(e.energy,(Factor001))

for e in electrons1:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor01))
        hist_e_theta_out.Fill(theta,(Factor01))
        hist_4out.Fill(squared_4mom,(Factor01))
        hist_Px_out_01.Fill(e.px,(Factor01))
        hist_Py_out_01.Fill(e.py,(Factor01))
        hist_Pz_out_01.Fill(e.pz,(Factor01))
        hist_E_out_01.Fill(e.energy,(Factor01))

for e in electrons2:

    if e.status is -1 :
        squared_4mom = (-e.px*e.px -e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)

    if e.status is 1:
        squared_4mom = (-e.px*e.px-e.py*e.py-e.pz*e.pz+e.energy*e.energy)
        print(squared_4mom)
        r = math.sqrt(e.px**2+e.py**2+e.pz**2)
        theta = math.acos(e.pz/r)
        if e.px!=0:
            azim = math.atan(e.py/e.px)
            hist_e_phi_out.Fill(azim,(Factor1))
        hist_e_theta_out.Fill(theta,(Factor1))
        hist_4out.Fill(squared_4mom,(Factor1))
        hist_Px_out_1.Fill(e.px,(Factor1))
        hist_Py_out_1.Fill(e.py,(Factor1))
        hist_Pz_out_1.Fill(e.pz,(Factor1))
        hist_E_out_1.Fill(e.energy,(Factor1))

c.cd(1)
hist_e_theta_out.GetXaxis().SetTitle("#theta[rad]")
hist_e_theta_out.Draw()
c.cd(2)
hist_e_phi_out.GetXaxis().SetTitle("#phi[rad]")
hist_e_phi_out.Draw()
c.cd(3)
hist_4in.GetXaxis().SetTitle("q^{2}_{e_{in}}")
hist_4in.Draw()
c.cd(4)
hist_4out.GetXaxis().SetTitle("q^{2}_{e_{out}}")
hist_4out.Draw()
c.SaveAs("electron_angle_plots_lab_30deg"+str(FF)+".root")

c_mom.cd(1)
hist_Px_out_001.GetXaxis().SetTitle("P_{x}")
hist_Px_out_001.Draw('HIST')
hist_Px_out_01.SetLineColor(3)
hist_Px_out_01.Draw('HISTSAME')
hist_Px_out_1.SetLineColor(2)
hist_Px_out_1.Draw('HISTSAME')
c_mom.cd(2)
hist_Py_out_001.GetXaxis().SetTitle("P_{y}")
hist_Py_out_001.Draw('HIST')
hist_Py_out_01.SetLineColor(3)
hist_Py_out_01.Draw('HISTSAME')
hist_Py_out_1.SetLineColor(2)
hist_Py_out_1.Draw('HISTSAME')
c_mom.cd(3)
hist_Pz_out_001.GetXaxis().SetTitle("P_{z}")
hist_Pz_out_001.Draw('HIST')
hist_Pz_out_01.SetLineColor(3)
hist_Pz_out_01.Draw('HISTSAME')
hist_Pz_out_1.SetLineColor(2)
hist_Pz_out_1.Draw('HISTSAME')
c_mom.cd(4)
hist_E_out_001.GetXaxis().SetTitle("E")
hist_E_out_001.Draw('HIST')
hist_E_out_01.SetLineColor(3)
hist_E_out_01.Draw('HISTSAME')
hist_E_out_1.SetLineColor(2)
hist_E_out_1.Draw('HISTSAME')
c_mom.SaveAs("electron_mom_plots_lab_30deg"+str(FF)+".root")
