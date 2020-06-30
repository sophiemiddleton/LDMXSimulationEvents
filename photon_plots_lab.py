from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math

EventWeight =0.001583
Lumi = 0.22
ProtonsPerN = 74
Factor = EventWeight*Lumi*ProtonsPerN

data=readLHEF('FFop4_cuts/30deg_1.lhe')
photons=data.getParticlesByIDs([22,-22])
c=TCanvas()
c.Divide(2,2)

c_mom=TCanvas()
c_mom.Divide(2,2)

hist_photon_theta=TH1F("theta_photon", "Photon Theta",100,0,2)
hist_photon_pt =TH1F("photon pt", "Photon Pt",100,0,2)
hist_EvTheta=TH2F("Photon Energy v Theta", "Photon Energy v Theta",
                100,0,2,100,0,2.5)
hist_phi=TH1F("phi_photon", "Photon Phi",100,-math.pi, math.pi)
hist_Pz_out=TH1F("P_{z} ", "Photon P_{z} ", 100,-5,10)
hist_Px_out=TH1F("P_{x}", "Photon P_{x} ", 100,-5,5)
hist_Py_out=TH1F("P_{y}", "Photon P_{y} ", 100,-5,5)
hist_E_out=TH1F("E", "Photon E ", 100,0,10)
for g in photons:
    #theta = math.atan(g.py/g.pz)
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    theta = math.acos(g.pz/r)
    azim = math.atan(g.py/g.px)
    hist_phi.Fill(azim)
    hist_photon_theta.Fill(theta, Factor)
    hist_photon_pt.Fill(g.pt, Factor)
    hist_EvTheta.Fill(theta,g.energy, Factor)
    hist_Pz_out.Fill(g.pz,Factor)
    hist_Px_out.Fill(g.px,Factor)
    hist_Py_out.Fill(g.py,Factor)
    hist_E_out.Fill(r,Factor)

c.cd(1)
hist_photon_theta.Draw('HIST')
hist_photon_theta.GetXaxis().SetTitle("#theta")
c.cd(2)
hist_phi.Draw("HIST")
hist_phi.GetXaxis().SetTitle("#phi")
c.cd(3)
hist_EvTheta.GetXaxis().SetTitle("#theta")
hist_EvTheta.GetYaxis().SetTitle("E_{#gamma}")
hist_EvTheta.Draw("COLZ")
c.cd(4)
hist_photon_pt.Draw("HIST")
hist_photon_pt.GetXaxis().SetTitle("p_{t}_{#gamma}")
c.SaveAs("photon_plots_lab_5degFF3.root")

c_mom.cd(1)
hist_Px_out.Draw("HIST")
hist_Px_out.GetXaxis().SetTitle("p_{x}")
c_mom.cd(2)
hist_Py_out.Draw("HIST")
hist_Py_out.GetXaxis().SetTitle("p_{y}")
c_mom.cd(3)
hist_Pz_out.Draw("HIST")
hist_Pz_out.GetXaxis().SetTitle("p_{z}")
c_mom.cd(4)
hist_E_out.Draw("HIST")
hist_E_out.GetXaxis().SetTitle("E")
c_mom.SaveAs("photon_mom_plots_lab_5deg_ff3.root")
