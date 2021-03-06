import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/082C09FA-5563-E511-9FBC-24BE05C44BB1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/08C2F8E2-5563-E511-B00C-B8CA3A70A5E8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/0EE1F8CD-5963-E511-B3D4-F45214C748CA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/0EE4EAFA-5563-E511-9EB7-24BE05C63651.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/10F70EE5-5563-E511-BFD6-D4AE526A0C7A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/1E05EF16-5A63-E511-8E26-F45214C7493C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/1EE8FFE0-5563-E511-B18C-00A0D1EE8A20.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/28721FE7-5563-E511-BD61-0002C92958E8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/28EE79DE-5563-E511-BEA6-B8CA3A70A520.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/361AD8F0-5563-E511-9AE6-1CC1DE18CEEE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/389140E2-5563-E511-9A22-0CC47A01CAEA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/400007FA-5563-E511-B036-5065F381C1D1.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/4005691B-5A63-E511-9B19-0002C90F7FDE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/42816EE2-5563-E511-9DB7-F45214C7B6BA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/42F695EB-5563-E511-B1E9-0002C92A1034.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/527548E6-5563-E511-8F0E-F45214C748D2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5A6FFBE5-5563-E511-829F-D4AE526A0D2E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/5AAAC512-5B63-E511-A8C1-0002C92DB464.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/66F951E5-5563-E511-8395-D4AE526A0DAE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/6AC29A1B-5A63-E511-AA05-F45214C748C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/6C74E9E0-5563-E511-9225-00A0D1EE8A20.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/7605CF1F-5A63-E511-B324-F45214C748CE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/76DAD219-5A63-E511-8100-F45214C748D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/8092BDE4-5563-E511-9601-D4AE5269F656.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/867427E3-5563-E511-9DB4-F45214C748D2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/86A554BE-5D63-E511-A0EF-F45214C748D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/90A2DBE2-5563-E511-A1CE-0CC47A00AA80.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/90BC78DB-5563-E511-B844-00266CF9B878.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/9E1D8AEC-5563-E511-818C-1CC1DE19286E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/A416A3E8-5563-E511-8FFA-001EC9AF200F.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/B2F63BE4-5563-E511-A19E-0CC47A00A832.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D22441F0-5563-E511-AF4C-1CC1DE18CFEA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D45D77E8-5563-E511-A450-842B2B760921.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/D87F44F0-5563-E511-B798-F45214C748C8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/DA828938-5A63-E511-8507-F45214C748D2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/EA7427E3-5563-E511-B58C-F45214C748D2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/F0EE17E1-5563-E511-B431-00A0D1EE8A20.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/50000/FC5A3C08-5663-E511-8CAD-5065F3819221.root' ] );


secFiles.extend( [
               ] )

