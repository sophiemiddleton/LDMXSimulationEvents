from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('nonMinECut/unweighted_events.lhe')
photons=data.getParticlesByIDs([22,-22])
c=TCanvas()
c.Divide(2,2)
hist_photon_theta=TH1F("theta_photon", "Photon Theta",100,1,2)
hist_photon_pt =TH1F("photon pt", "Photon Pt",100,0.2,0.7)
hist_EvTheta=TH2F("Photon Energy v Theta", "Photon Energy v Theta",
                100,1, 2,100,0,4)
hist_phi=TH1F("phi_photon", "Photon Phi",100,-math.pi, math.pi)

for g in photons:
    #theta = math.atan(g.py/g.pz)
    r = math.sqrt(g.px*g.px + g.py*g.py+g.pz*g.pz)
    theta = math.acos(g.py/r)
    azim = math.atan(g.pz/g.px)
    hist_phi.Fill(azim)
    hist_photon_theta.Fill(theta)
    hist_photon_pt.Fill(g.pt)
    hist_EvTheta.Fill(theta,g.energy)

c.cd(1)
hist_photon_theta.Draw()
hist_photon_theta.GetXaxis().SetTitle("#theta")
c.cd(2)
hist_phi.Draw()
hist_phi.GetXaxis().SetTitle("#phi")
c.cd(3)
hist_EvTheta.GetXaxis().SetTitle("#theta")
hist_EvTheta.GetYaxis().SetTitle("E_{#gamma}")
hist_EvTheta.Draw("COLZ")
c.cd(4)
hist_photon_pt.Draw()
hist_photon_pt.GetXaxis().SetTitle("p_{t}_{#gamma}")
c.SaveAs("photon_plots.png")
