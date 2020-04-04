from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F
import math
data=readLHEF('unweighted_events.lhe')
electrons=data.getParticlesByIDs([11,-11])
photons=data.getParticlesByIDs([22,-22])
c=TCanvas()
hist_e=TH1F("costheta_elec", "Cos Theta",100,-1,1)
hist_photon=TH1F("costheta_photon", "Cos Theta",100,-1,1)
hist_4mom=TH2F("4mom ratio", "4mom in v 4mom out", 100,0,100,100,0,100)

for e in electrons:
    val = math.atan(e.py/e.pz)
    hist_e.Fill(val)
    squared_out = 1;
    squared_in = 1;
    hist_4mom.Fill(squared_out, squared_in)
hist_e.Draw()
for g in photons:
    val = math.atan(g.py/g.pz)
    hist_photon.Fill(val)

hist_photon.Draw("same")
c.SaveAs("costheta_elec.png")
