COIN_STATUS_FAIL = "Failed!"
COIN_STATUS_SUCCESS = "Finished!"
COIN_STATUS_PROCESSING = "Processing ..."


PROCESSING_GENESIS_BLOCK = "Generating GenesisBlock ..."
PROCESSING_EDIT_CORE = "Making Source Code of Core ..."
PROCESSING_GIT_PUSH = "Pushing Source Code of Core to Github ..."
PROCESSING_BUILD_CORE = "Building Core ..."

FAILED_GITHUB_PUSH = "failed at pushing github!"
FAILED_GITHUB_PREPARE = "failed at preparing github!"

#PLATFORMS = {"core":"CORE", "seeder":"SEEDER", "android":"ANDROID", "ios":"IOS"}


CORE_FLAGS = {"maxMoney":"_FLAG_MAX_MONEY_", "pszTimestamp":"_FLAG_PSZTIMESTAMP_", "halvingInterval":"_FLAG_NSUBSIDYHALVINGINTERVAL_", "nDefaultPort":"_FLAG_NDEFAULTPORT_",
              "nTime":"_FLAG_NTIME_", "nNonce":"_FLAG_NNONCE_", "nBits":"_FLAG_NBITS_", "gHash":"_FLAG_HASHGENESISBLOCK_", "mHash":"_FLAG_HASHMERKLEROOT_",
              "dnsSeeds":"_FLAG_DNS_SEEDS_", "coinBase":"_FLAG_COINBASE_", "fullNodes":"_FLAG_FULL_NODES_", "nSubsidy":"_FLAG_NSUBSIDY_" }

ANDROID_FLAGS = {"gHash":"_FLAG_HASHGENESISBLOCK_", "nTime":"_FLAG_NTIME_", "nBits":"_FLAG_NBITS_", "dnsSeeds":"_FLAG_DNS_SEEDS_", "maxMoney":"_FLAG_MAX_MONEY_",
                 "nDefaultPort":"_FLAG_NDEFAULTPORT_",
                 }

SEEDER_FLAGS = {"dnsSeeds":"_FLAG_DNS_SEEDS_", "defPort":"_FLAG_DEFPORT_", "testDefPort":"_FLAG_TESTDEFPORT_"}

PLATFORMS = ['windows', 'linux', 'seeder', 'android', 'ios']

DOWNLOAD_HOST_URL = "http://192.168.1.7"