from lhereader import readLHEF
from ROOT import TCanvas, TH1F, TH2F, TLorentzVector, TF1
import math
data03 =readLHEF('FFop3_cuts/30_001.lhe')
data04 =readLHEF('FFop3_cuts/30_01.lhe')
data05 =readLHEF('FFop3_cuts/30_1.lhe')
data06 =readLHEF('FFop4_cuts/30deg.lhe')

Lumi = 0.22
ProtonsPerN = 74
Factor001=0.3678*Lumi*ProtonsPerN
Factor01=0.2651*Lumi*ProtonsPerN
Factor1=0.12*Lumi*ProtonsPerN

electrons03=data03.getParticlesByIDs([9000002,-9000002])
electrons04=data04.getParticlesByIDs([9000002,-9000002])
electrons05=data05.getParticlesByIDs([9000002,-9000002])
electrons06=data06.getParticlesByIDs([9000002,-9000002])

c=TCanvas()
c.Divide(2,2)
c1=TCanvas()
c1.Divide(2,2)

hist_4mom_diff_opt3_001=TH1F("#Delta q^{2} in opt3", "P_{lab}^{#gamma} = 0.01GeV ", 50,-10,0)
hist_4mom_diff_opt4_001=TH1F("#Delta q^{2} in opt4", "P_{lab}^{#gamma} = 0.01GeV ", 50,-10,0)
hist_4momRatio34_001=TH1F("q^{2} out opt3/opt4", "P_{lab}^{#gamma} = 0.01GeV ", 50,-10,0)

hist_4mom_diff_opt3_01=TH1F("#Delta q^{2} in opt3", "P_{lab}^{#gamma} = 0.1GeV ", 50,-10,0)
hist_4mom_diff_opt4_01=TH1F("#Delta q^{2} in opt4", "P_{lab}^{#gamma} = 0.1GeV ", 50,-10,0)
hist_4momRatio34_01=TH1F("q^{2} out opt3/opt4", "P_{lab}^{#gamma} = 0.1GeV ", 50,-10,0)

hist_4mom_diff_opt3_1=TH1F("#Delta q^{2} in opt3", "P_{lab}^{#gamma} = 1GeV ", 50,-10,0)
hist_4mom_diff_opt4_1=TH1F("#Delta q^{2} in opt4", "P_{lab}^{#gamma} = 1GeV ", 50,-10,0)
hist_4momRatio34_1=TH1F("q^{2} out opt3/opt4", "P_{lab}^{#gamma} = 1GeV ", 50,-10,0)
outgoing_values_p_opt3_001 = []
incoming_values_p_opt3_001 = []
outgoing_values_p_opt4_001 = []
incoming_values_p_opt4_001 = []
outgoing_values_p_opt3_01 = []
incoming_values_p_opt3_01 = []
outgoing_values_p_opt4_01 = []
incoming_values_p_opt4_01 = []
outgoing_values_p_opt3_1 = []
incoming_values_p_opt3_1 = []
outgoing_values_p_opt4_1 = []
incoming_values_p_opt4_1 = []

for i, e in enumerate(electrons03):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt3_001.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt3_001.append(outgoing)

for j, event in enumerate(incoming_values_p_opt3_001):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt3_001[j] - incoming_values_p_opt3_001[j]
    hist_4mom_diff_opt3_001.Fill(qdiff.M2(),Factor001)

for i, e in enumerate(electrons06):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt4_001.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt4_001.append(outgoing)

for j, event in enumerate(incoming_values_p_opt4_001):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt4_001[j] - incoming_values_p_opt4_001[j]
    hist_4mom_diff_opt4_001.Fill(qdiff.M2(),Factor001)

for i, e in enumerate(electrons04):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt3_01.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt3_01.append(outgoing)

for j, event in enumerate(incoming_values_p_opt3_01):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt3_01[j] - incoming_values_p_opt3_01[j]
    hist_4mom_diff_opt3_01.Fill(qdiff.M2(),Factor01)

for i, e in enumerate(electrons06):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt4_01.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt4_01.append(outgoing)

for j, event in enumerate(incoming_values_p_opt4_01):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt4_01[j] - incoming_values_p_opt4_01[j]
    hist_4mom_diff_opt4_01.Fill(qdiff.M2(),Factor01)

for i, e in enumerate(electrons05):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt3_1.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt3_1.append(outgoing)

for j, event in enumerate(incoming_values_p_opt3_1):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt3_1[j] - incoming_values_p_opt3_1[j]
    hist_4mom_diff_opt3_1.Fill(qdiff.M2(),Factor1)

for i, e in enumerate(electrons06):
    incoming = TLorentzVector()
    outgoing = TLorentzVector()

    if e.status is -1 :
        incoming.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        incoming_values_p_opt4_1.append(incoming)
    if e.status is 1:
        outgoing.SetPxPyPzE(e.px,e.py,e.pz,e.energy)
        outgoing_values_p_opt4_1.append(outgoing)

for j, event in enumerate(incoming_values_p_opt4_1):
    qdiff = TLorentzVector()
    qdiff = outgoing_values_p_opt4_1[j] - incoming_values_p_opt4_1[j]
    hist_4mom_diff_opt4_01.Fill(qdiff.M2(),Factor1)

c1.cd(1)
hist_4mom_diff_opt3_001.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt3_001.Draw("HIST")
hist_4mom_diff_opt3_01.SetLineColor(3)
hist_4mom_diff_opt3_01.Draw("HISTSAME")
hist_4mom_diff_opt3_1.SetLineColor(2)
hist_4mom_diff_opt3_1.Draw('HISTSAME"')
c1.cd(2)
hist_4mom_diff_opt4_001.GetXaxis().SetTitle("#Delta q^{2} [GeV/c]")
hist_4mom_diff_opt4_001.Draw("HIST")
hist_4mom_diff_opt4_01.SetLineColor(3)
hist_4mom_diff_opt4_01.Draw("HISTSAME")
hist_4mom_diff_opt3_1.SetLineColor(2)
hist_4mom_diff_opt4_1.Draw('HISTSAME"')
for i in range(0,hist_4mom_diff_opt4_001.GetNbinsX()):
    if hist_4mom_diff_opt4_001.GetBinContent(i) !=0 :
        ratio34 = hist_4mom_diff_opt3_001.GetBinContent(i)/hist_4mom_diff_opt4_001.GetBinContent(i)
        hist_4momRatio34_001.SetBinContent(i,ratio34*Factor001)
c1.cd(3)
hist_4momRatio34_001.Draw()
c1.SaveAs("compare4mom_op34_withcut.root")
