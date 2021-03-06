import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/1246AE3D-B425-E511-9C9B-02163E0138B3.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/3073361B-2B26-E511-A5D9-001E67A41EA0.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/A6EC90D3-DE24-E511-8BF0-02163E0114C7.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/A881A22D-6325-E511-A106-0026189438B5.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/20000/D44E8A75-8926-E511-A66B-02163E011C17.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/04012EB5-8424-E511-9C6C-02163E0138A8.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0A3B4E84-8724-E511-99BD-02163E0149BD.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0EAA383F-9A26-E511-A8CA-001E67A40442.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/124477A6-E325-E511-82C5-0025905A6104.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1AA66DA1-E225-E511-A2C3-0025905A60B8.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1C7605F2-9A26-E511-BE3C-001E67A3FDF8.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/34B306C7-8524-E511-870D-02163E0134D5.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/3A530B01-9724-E511-B319-02163E0151B2.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/4650CF72-352E-E511-83EF-00266CFFA148.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/48DE1F8C-AE24-E511-ACE4-02163E01265F.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/70299EA5-8524-E511-A682-02163E013987.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/704794F3-8224-E511-84B9-02163E014186.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/70611720-7C25-E511-8D64-001E6757A138.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/70D9CBAF-8424-E511-8032-02163E011A9A.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7804DAD2-8424-E511-B358-02163E013598.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7814C074-0327-E511-B7A7-02163E011A34.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7A46049A-9524-E511-8142-02163E0148FC.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/84ED2E76-9224-E511-8273-02163E0136CF.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A4224BC7-8424-E511-9B79-02163E013553.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A439D9F6-8224-E511-B65B-02163E011A46.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A693CCB4-8424-E511-A693-02163E0133EE.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/AE2254C6-8624-E511-A772-02163E0136B1.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B8D9D5FE-9A26-E511-AB97-001E675A4759.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/CE86448C-9A26-E511-8ECA-90B11C08CA45.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/D0174F1A-9424-E511-9546-02163E014527.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/D03D2ACD-8524-E511-B70B-02163E011B3F.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/DECF47A6-E325-E511-9EE8-0025905A60D0.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E0EA481A-352E-E511-926A-002590DB92A8.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E26AD566-9B26-E511-96B7-001E675A6C2A.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E293356B-9224-E511-80D6-02163E01416E.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E8170C5D-9524-E511-8005-02163E0147DE.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/F8E619D0-8524-E511-95B1-02163E011A59.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/FA28948F-8524-E511-A37F-02163E011A46.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0045D03F-D025-E511-AC38-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/104E1CFD-3525-E511-96C6-02163E013992.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/16BF183C-2E25-E511-84A5-02163E0146A4.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/2AAEE442-D025-E511-AD20-0025905A60BE.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/36EEA09A-2E26-E511-A78A-02163E012BD2.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/3A8E795F-2F25-E511-85CA-02163E00E84A.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/566CF165-2F25-E511-87DF-02163E00F54B.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/5A828A9F-6827-E511-98F0-02163E012093.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/5CFC4570-DC2D-E511-95B8-002590DB920C.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/62894445-A526-E511-852F-001E675A6AB3.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/62E3AF41-D025-E511-B551-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/766880A3-2D25-E511-8213-02163E00C02F.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/7A52683B-2E25-E511-8BDB-02163E013960.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/8226BB07-2E25-E511-B05E-02163E011DA9.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/A4BCFA44-D025-E511-8AB9-0025905A607E.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/AAA76AFC-3525-E511-A4C4-02163E0136B4.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D458236E-DC2D-E511-9E47-002481E101DA.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D47FBA4D-2E25-E511-8D5C-02163E012B2A.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/D6168337-6525-E511-9780-02163E013960.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/DEB4946A-1D28-E511-81AE-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/E256A940-D025-E511-B121-0025905A609E.root',
       '/store/mc/RunIISpring15DR74/ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/F288E6D6-1C28-E511-AD6F-002618943836.root' ] );


secFiles.extend( [
               ] )

