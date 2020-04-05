from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('run02/unweighted_events.lhe')
photons=data.getParticlesByIDs([22,-22])
c=TCanvas()
c.Divide(2,2)
hist_photon_theta=TH1F("theta_photon", "Photon Theta",100,-1,1)
hist_photon_pt =TH1F("photon pt", "Photon Pt",100,-1,1)
hist_EvTheta=TH2F("Photon Energy v Theta", "Photon Energy v Theta",
                100,-1,1,100,0,5)

for g in photons:
    val = math.atan(g.py/g.pz)
    hist_photon_theta.Fill(val)
    hist_photon_pt.Fill(g.pt)
    hist_EvTheta.Fill(val,g.energy)
c.cd(1)
hist_photon_theta.Draw()
hist_photon_theta.GetXaxis().SetTitle("#theta")
c.cd(2)
hist_EvTheta.GetXaxis().SetTitle("#theta")
hist_EvTheta.GetYaxis().SetTitle("E_{#gamma}")
hist_EvTheta.Draw()
c.cd(3)
hist_photon_pt.Draw()
hist_photon_pt.GetXaxis().SetTitle("p_{t}_{#gamma}")
c.SaveAs("photon_plots.png")
