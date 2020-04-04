#include "TFile.h"
#include "TTree.h"
#include "TRandom.h"
#include "TH1D.h"
#include "TTreeReader.h"
using namespace std;
void AddBranch() {
    TFile f("unweighted_events.root", "update");
    Float_t new_v;
    auto t3 = f.Get<TTree>("LHEF;1");
    auto newBranch = t3->Branch("new_v", &new_v, "new_v/F");
    Long64_t nentries = t3->GetEntries(); // read the number of entries in the t3
    for (Long64_t i = 0; i < nentries; i++) {
        new_v = 1;
        newBranch->Fill();
    }
    t3->Write("", TObject::kOverwrite); // save only the new version of the tree
}

void AccessTree(){
  TFile *f = new TFile("unweighted_events.root");
  TTree *tree = (TTree*) f->Get("LHEF;1");
  Double_t Py = 0;
  Double_t Pz = 0;
  tree->SetBranchAddress("Particle.Py",&Py);
  tree->SetBranchAddress("Particle.Pz",&Pz);

  TH1D *histo = new TH1D("histo","",100,-100,100);
  for(int i=0; i<tree->GetEntries(); ++i){

     tree->GetEntry(i);
     printf("%f\n",Py );
     double angle = atan(Py/Pz);
     histo->Fill(angle);
   }
}

void AddAngleBranch() {
    TFile f("unweighted_events.root", "update");
    Float_t PolarAngle;
    auto t3 = f.Get<TTree>("LHEF;1");
    auto newBranch = t3->Branch("PolarAngle", &PolarAngle, "PolarAngle/F");
    Long64_t nentries = t3->GetEntries(); // read the number of entries in the t3
    Double_t Py;
    Double_t Pz;

    t3->SetBranchAddress("Particle.Py",&Py);
    t3->SetBranchAddress("Particle.Pz",&Pz);
    printf("%lld\n",nentries);
    for (Long64_t i = 0; i < nentries; i++) {
        t3->GetEntry(i);
        PolarAngle = atan(Py/Py);
        //printf("%f\n",PolarAngle);
        newBranch->Fill();
    }
    t3->Write("", TObject::kOverwrite); // save only the new version of the tree
}
