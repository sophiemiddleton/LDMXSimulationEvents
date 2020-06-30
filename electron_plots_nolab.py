from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('FFopt3NoCut/unweighted_events.lhe')
electrons=data.getParticlesByIDs([11,-11])
c=TCanvas()
c.Divide(2,2)
c_mom=TCanvas()
c_mom.Divide(2,2)

hist_e_theta_out=TH1F("theta_elec_out", "Outgoing Electron Theta",100,0, math.pi)
hist_e_phi_out=TH1F("phi_elec_out", "Outgoing Electron Phi",100,-math.pi,math.pi)
hist_4in=TH1F("q^{2} in", "Incoming Electron q^{2} ", 100,0,100)
hist_4out=TH1F("q^{2} out", "Outgoing Electron q^{2} ", 100,0,100)

hist_Pz_out=TH1F("P_{z} out", "Outgoing Electron P_{z} ", 100,0,5)
hist_Px_out=TH1F("P_{x} out", "Outgoing Electron P_{x} ", 100,-1,1)
hist_Py_out=TH1F("P_{y} out", "Outgoing Electron P_{y} ", 100,-1,1)

for e in electrons:

    if e.status is -1 :
        squared_4mom = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
        hist_4in.Fill(squared_4mom)
        print((e.px*e.px , e.py*e.py,e.pz*e.pz,e.energy*e.energy))
    if e.status is 1:
        r = math.sqrt(e.px*e.px + e.py*e.py+e.pz*e.pz)
        theta = math.acos(e.pz/r)
        hist_e_theta_out.Fill(theta)
        azim = math.atan(e.py/e.px)
        hist_e_phi_out.Fill(azim)
        squared_4mom = (e.px*e.px + e.py*e.py+e.pz*e.pz+e.energy*e.energy)
        hist_4out.Fill(squared_4mom)
        hist_Pz_out.Fill(e.pz)
        hist_Py_out.Fill(e.py)
        hist_Px_out.Fill(e.px)


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
c.SaveAs("electron_angle_plots_nolab.png")

c_mom.cd(1)
hist_Px_out.GetXaxis().SetTitle("P_{x}")
hist_Px_out.Draw()
c_mom.cd(2)
hist_Py_out.GetXaxis().SetTitle("P_{y}")
hist_Py_out.Draw()
c_mom.cd(3)
hist_Pz_out.GetXaxis().SetTitle("P_{z}")
hist_Pz_out.Draw()
c_mom.SaveAs("electron_mom_plots_nolab.png")
