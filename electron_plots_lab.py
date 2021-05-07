from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector, TF1
import math

data=[]
EventWeight =0.001583
Lumi = 0.22
ProtonsPerN = 74
Factor = EventWeight*Lumi*ProtonsPerN
FF=3
if FF==1:
    Eventweight =281.1
    data=readLHEF('FFop1_cuts/30deg_1.lhe')
if FF == 2:
    Eventweight= 0.0002394
    data=readLHEF('FFop2_cuts/30deg_1.lhe')
if FF==3:
    Eventweight = 0.1795
    data=readLHEF('FFop3_cuts/30deg_1.lhe')
if FF==4:
    Eventweight = 0.001583
    data=readLHEF('FFop4_cuts/30deg_1.lhe')

print("FF is :",FF," Event Weight is : ", EventWeight)
electrons=data.getParticlesByIDs([11,-11])
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

hist_Pz_out=TH1F("P_{z} out", "Outgoing Electron P_{z} ", 100,-2,2)
hist_Px_out=TH1F("P_{x} out", "Outgoing Electron P_{x} ", 100,-2,2)
hist_Py_out=TH1F("P_{y} out", "Outgoing Electron P_{y} ", 100,-2,2)
hist_E_out=TH1F("E out", "Outgoing Electron E ", 100,0,2)

for e in electrons:

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
            hist_e_phi_out.Fill(azim,(Factor))
        hist_e_theta_out.Fill(theta,(Factor))
        hist_4out.Fill(squared_4mom,(Factor))
        hist_Pz_out.Fill(e.pz,(Factor))
        hist_Py_out.Fill(e.py,(Factor))
        hist_Px_out.Fill(e.px,(Factor))
        hist_E_out.Fill(e.energy,(Factor))
c.cd(1)
hist_e_theta_out.GetXaxis().SetTitle("#theta[rad]")
hist_e_theta_out.Draw('HIST')
c.cd(2)
hist_e_phi_out.GetXaxis().SetTitle("#phi[rad]")
hist_e_phi_out.Draw('HIST')
c.cd(3)
hist_4in.GetXaxis().SetTitle("q^{2}_{e_{in}}")
hist_4in.Draw('HIST')
c.cd(4)
hist_4out.GetXaxis().SetTitle("q^{2}_{e_{out}}")
hist_4out.Draw('HIST')
c.SaveAs("electron_angle_plots_lab_30deg"+str(FF)+".root")

c_mom.cd(1)
hist_Px_out.GetXaxis().SetTitle("P_{x}")
hist_Px_out.Draw('HIST')
c_mom.cd(2)
hist_Py_out.GetXaxis().SetTitle("P_{y}")
hist_Py_out.Draw('HIST')
c_mom.cd(3)
hist_Pz_out.GetXaxis().SetTitle("P_{z}")
hist_Pz_out.Draw('HIST')
c_mom.cd(4)
hist_E_out.GetXaxis().SetTitle("E")
hist_E_out.Draw('HIST')
c_mom.SaveAs("electron_mom_plots_lab_30deg"+str(FF)+".root")
