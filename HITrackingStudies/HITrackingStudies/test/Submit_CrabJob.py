from CRABClient.UserUtilities import config

config = config()


config.General.workArea = 'TrackingStudies'
config.General.requestName = '2018PbPb_MAODData_GeneralTracks'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'run_PbPb_cfg.py'

config.Data.unitsPerJob = 5
config.Data.totalUnits = 10000
#config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.outLFNDirBase = '/store/user/rpradhan/'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/rpradhan/TrackingStudies'
config.Data.publication = False
config.Data.inputDataset = '/HIMinimumBias0/HIRun2018A-PbPb18_MiniAODv1-v1/MINIAOD'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt'
config.Data.outputDatasetTag = '2018PbPb_MAODData_GeneralTracks'

#config.Site.storageSite = 'T2_IN_TIFR'
config.Site.storageSite = 'T2_CH_CERN'
