

#include <QtGlobal>

// Automatically generated by extract_strings.py
#ifdef __GNUC__
#define UNUSED __attribute__((unused))
#else
#define UNUSED
#endif
static const char UNUSED *utabit_strings[] = {
QT_TRANSLATE_NOOP("utabit-core", ""
"(1 = keep tx meta data e.g. account owner and payment request information, 2 "
"= drop tx meta data)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"-fallbackfee is set very high! This is the transaction fee you may pay when "
"fee estimates are not available."),
QT_TRANSLATE_NOOP("utabit-core", ""
"-maxtxfee is set very high! Fees this large could be paid on a single "
"transaction."),
QT_TRANSLATE_NOOP("utabit-core", ""
"-paytxfee is set very high! This is the transaction fee you will pay if you "
"send a transaction."),
QT_TRANSLATE_NOOP("utabit-core", ""
"A fee rate (in %s/kB) that will be used when fee estimation has insufficient "
"data (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Accept relayed transactions received from whitelisted peers even when not "
"relaying transactions (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Allow JSON-RPC connections from specified source. Valid for <ip> are a "
"single IP (e.g. 1.2.3.4), a network/netmask (e.g. 1.2.3.4/255.255.255.0) or "
"a network/CIDR (e.g. 1.2.3.4/24). This option can be specified multiple times"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Bind to given address and always listen on it. Use [host]:port notation for "
"IPv6"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Bind to given address and whitelist peers connecting to it. Use [host]:port "
"notation for IPv6"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Bind to given address to listen for JSON-RPC connections. Use [host]:port "
"notation for IPv6. This option can be specified multiple times (default: "
"bind to all interfaces)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Cannot obtain a lock on data directory %s. Utabit Core is probably already "
"running."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Create new files with system default permissions, instead of umask 077 (only "
"effective with disabled wallet functionality)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Delete all wallet transactions and only recover those parts of the "
"blockchain through -rescan on startup"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Discover own IP addresses (default: 1 when listening and no -externalip or -"
"proxy)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Distributed under the MIT software license, see the accompanying file "
"COPYING or <http://www.opensource.org/licenses/mit-license.php>."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Do not keep transactions in the mempool longer than <n> hours (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Error reading wallet.dat! All keys read correctly, but transaction data or "
"address book entries might be missing or incorrect."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Error: Listening for incoming connections failed (listen returned error %s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Execute command when a relevant alert is received or we see a really long "
"fork (%s in cmd is replaced by message)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Execute command when a wallet transaction changes (%s in cmd is replaced by "
"TxID)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Execute command when the best block changes (%s in cmd is replaced by block "
"hash)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Fees (in %s/kB) smaller than this are considered zero fee for relaying, "
"mining and transaction creation (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Fees (in %s/kB) smaller than this are considered zero fee for transaction "
"creation (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Force relay of transactions from whitelisted peers even they violate local "
"relay policy (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"How thorough the block verification of -checkblocks is (0-4, default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"If <category> is not supplied or if <category> = 1, output all debugging "
"information."),
QT_TRANSLATE_NOOP("utabit-core", ""
"If paytxfee is not set, include enough fee so transactions begin "
"confirmation on average within n blocks (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Invalid amount for -maxtxfee=<amount>: '%s' (must be at least the minrelay "
"fee of %s to prevent stuck transactions)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Maintain a full transaction index, used by the getrawtransaction rpc call "
"(default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Maximum size of data in data carrier transactions we relay and mine "
"(default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Maximum total fees (in %s) to use in a single wallet transaction; setting "
"this too low may abort large transactions (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Number of seconds to keep misbehaving peers from reconnecting (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Output debugging information (default: %u, supplying <category> is optional)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Please check that your computer's date and time are correct! If your clock "
"is wrong Utabit Core will not work properly."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Prune configured below the minimum of %d MiB.  Please use a higher number."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Prune: last wallet synchronisation goes beyond pruned data. You need to -"
"reindex (download the whole blockchain again in case of pruned node)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Query for peer addresses via DNS lookup, if low on addresses (default: 1 "
"unless -connect)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Randomize credentials for every proxy connection. This enables Tor stream "
"isolation (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Reduce storage requirements by pruning (deleting) old blocks. This mode is "
"incompatible with -txindex and -rescan. Warning: Reverting this setting "
"requires re-downloading the entire blockchain. (default: 0 = disable pruning "
"blocks, >%u = target size in MiB to use for block files)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Rescans are not possible in pruned mode. You will need to use -reindex which "
"will download the whole blockchain again."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Set maximum size of high-priority/low-fee transactions in bytes (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Set the number of script verification threads (%u to %d, 0 = auto, <0 = "
"leave that many cores free, default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Set the number of threads for coin generation if enabled (-1 = all cores, "
"default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Support filtering of blocks and transaction with bloom filters (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"The block database contains a block which appears to be from the future. "
"This may be due to your computer's date and time being set incorrectly. Only "
"rebuild the block database if you are sure that your computer's date and "
"time are correct"),
QT_TRANSLATE_NOOP("utabit-core", ""
"The transaction amount is too small to send after the fee has been deducted"),
QT_TRANSLATE_NOOP("utabit-core", ""
"This is a pre-release test build - use at your own risk - do not use for "
"mining or merchant applications"),
QT_TRANSLATE_NOOP("utabit-core", ""
"This product includes software developed by the OpenSSL Project for use in "
"the OpenSSL Toolkit <https://www.openssl.org/> and cryptographic software "
"written by Eric Young and UPnP software written by Thomas Bernard."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Total length of network version string (%i) exceeds maximum length (%i). "
"Reduce the number or size of uacomments."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Tries to keep outbound traffic under the given target (in MiB per 24h), 0 = "
"no limit (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Unable to bind to %s on this computer. Utabit Core is probably already "
"running."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Unsupported argument -socks found. Setting SOCKS version isn't possible "
"anymore, only SOCKS5 proxies are supported."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Unsupported argument -whitelistalwaysrelay ignored, use -whitelistrelay and/"
"or -whitelistforcerelay."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Use UPnP to map the listening port (default: 1 when listening and no -proxy)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Use separate SOCKS5 proxy to reach peers via Tor hidden services (default: "
"%s)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Username and hashed password for JSON-RPC connections. The field <userpw> "
"comes in the format: <USERNAME>:<SALT>$<HASH>. A canonical python script is "
"included in share/rpcuser. This option can be specified multiple times"),
QT_TRANSLATE_NOOP("utabit-core", ""
"WARNING: abnormally high number of blocks generated, %d blocks received in "
"the last %d hours (%d expected)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"WARNING: check your network connection, %d blocks received in the last %d "
"hours (%d expected)"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Warning: The network does not appear to fully agree! Some miners appear to "
"be experiencing issues."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Warning: Unknown block versions being mined! It's possible unknown rules are "
"in effect"),
QT_TRANSLATE_NOOP("utabit-core", ""
"Warning: We do not appear to fully agree with our peers! You may need to "
"upgrade, or other nodes may need to upgrade."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Warning: wallet.dat corrupt, data salvaged! Original wallet.dat saved as "
"wallet.{timestamp}.bak in %s; if your balance or transactions are incorrect "
"you should restore from a backup."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Whitelist peers connecting from the given netmask or IP address. Can be "
"specified multiple times."),
QT_TRANSLATE_NOOP("utabit-core", ""
"Whitelisted peers cannot be DoS banned and their transactions are always "
"relayed, even if they are already in the mempool, useful e.g. for a gateway"),
QT_TRANSLATE_NOOP("utabit-core", ""
"You need to rebuild the database using -reindex to go back to unpruned "
"mode.  This will redownload the entire blockchain"),
QT_TRANSLATE_NOOP("utabit-core", "(default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", "(default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "-maxmempool must be at least %d MB"),
QT_TRANSLATE_NOOP("utabit-core", "<category> can be:"),
QT_TRANSLATE_NOOP("utabit-core", "Accept command line and JSON-RPC commands"),
QT_TRANSLATE_NOOP("utabit-core", "Accept connections from outside (default: 1 if no -proxy or -connect)"),
QT_TRANSLATE_NOOP("utabit-core", "Accept public REST requests (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Activating best chain..."),
QT_TRANSLATE_NOOP("utabit-core", "Add a node to connect to and attempt to keep the connection open"),
QT_TRANSLATE_NOOP("utabit-core", "Allow DNS lookups for -addnode, -seednode and -connect"),
QT_TRANSLATE_NOOP("utabit-core", "Always query for peer addresses via DNS lookup (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Append comment to the user agent string"),
QT_TRANSLATE_NOOP("utabit-core", "Attempt to recover private keys from a corrupt wallet.dat on startup"),
QT_TRANSLATE_NOOP("utabit-core", "Automatically create Tor hidden service (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", "Block creation options:"),
QT_TRANSLATE_NOOP("utabit-core", "Cannot downgrade wallet"),
QT_TRANSLATE_NOOP("utabit-core", "Cannot resolve -bind address: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Cannot resolve -externalip address: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Cannot resolve -whitebind address: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Cannot write default address"),
QT_TRANSLATE_NOOP("utabit-core", "Connect only to the specified node(s)"),
QT_TRANSLATE_NOOP("utabit-core", "Connect through SOCKS5 proxy"),
QT_TRANSLATE_NOOP("utabit-core", "Connect to a node to retrieve peer addresses, and disconnect"),
QT_TRANSLATE_NOOP("utabit-core", "Connection options:"),
QT_TRANSLATE_NOOP("utabit-core", "Copyright (C) 2009-%i The Utabit Core Developers"),
QT_TRANSLATE_NOOP("utabit-core", "Corrupted block database detected"),
QT_TRANSLATE_NOOP("utabit-core", "Debugging/Testing options:"),
QT_TRANSLATE_NOOP("utabit-core", "Do not load the wallet and disable wallet RPC calls"),
QT_TRANSLATE_NOOP("utabit-core", "Do you want to rebuild the block database now?"),
QT_TRANSLATE_NOOP("utabit-core", "Done loading"),
QT_TRANSLATE_NOOP("utabit-core", "Enable publish hash block in <address>"),
QT_TRANSLATE_NOOP("utabit-core", "Enable publish hash transaction in <address>"),
QT_TRANSLATE_NOOP("utabit-core", "Enable publish raw block in <address>"),
QT_TRANSLATE_NOOP("utabit-core", "Enable publish raw transaction in <address>"),
QT_TRANSLATE_NOOP("utabit-core", "Enable transaction replacement in the memory pool (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Error initializing block database"),
QT_TRANSLATE_NOOP("utabit-core", "Error initializing wallet database environment %s!"),
QT_TRANSLATE_NOOP("utabit-core", "Error loading block database"),
QT_TRANSLATE_NOOP("utabit-core", "Error loading wallet.dat"),
QT_TRANSLATE_NOOP("utabit-core", "Error loading wallet.dat: Wallet corrupted"),
QT_TRANSLATE_NOOP("utabit-core", "Error loading wallet.dat: Wallet requires newer version of Utabit Core"),
QT_TRANSLATE_NOOP("utabit-core", "Error opening block database"),
QT_TRANSLATE_NOOP("utabit-core", "Error reading from database, shutting down."),
QT_TRANSLATE_NOOP("utabit-core", "Error"),
QT_TRANSLATE_NOOP("utabit-core", "Error: A fatal internal error occurred, see debug.log for details"),
QT_TRANSLATE_NOOP("utabit-core", "Error: Disk space is low!"),
QT_TRANSLATE_NOOP("utabit-core", "Failed to listen on any port. Use -listen=0 if you want this."),
QT_TRANSLATE_NOOP("utabit-core", "Fee (in %s/kB) to add to transactions you send (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Generate coins (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "How many blocks to check at startup (default: %u, 0 = all)"),
QT_TRANSLATE_NOOP("utabit-core", "Importing..."),
QT_TRANSLATE_NOOP("utabit-core", "Imports blocks from external blk000??.dat file on startup"),
QT_TRANSLATE_NOOP("utabit-core", "Include IP addresses in debug output (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Incorrect or no genesis block found. Wrong datadir for network?"),
QT_TRANSLATE_NOOP("utabit-core", "Information"),
QT_TRANSLATE_NOOP("utabit-core", "Initialization sanity check failed. Utabit Core is shutting down."),
QT_TRANSLATE_NOOP("utabit-core", "Insufficient funds"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid -onion address: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid -proxy address: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -fallbackfee=<amount>: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -maxtxfee=<amount>: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -minrelaytxfee=<amount>: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -mintxfee=<amount>: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -paytxfee=<amount>: '%s' (must be at least %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid amount for -paytxfee=<amount>: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Invalid netmask specified in -whitelist: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Keep at most <n> unconnectable transactions in memory (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Keep the transaction memory pool below <n> megabytes (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Listen for JSON-RPC connections on <port> (default: %u or testnet: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Listen for connections on <port> (default: %u or testnet: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Loading addresses..."),
QT_TRANSLATE_NOOP("utabit-core", "Loading block index..."),
QT_TRANSLATE_NOOP("utabit-core", "Loading wallet..."),
QT_TRANSLATE_NOOP("utabit-core", "Location of the auth cookie (default: data dir)"),
QT_TRANSLATE_NOOP("utabit-core", "Maintain at most <n> connections to peers (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Make the wallet broadcast transactions"),
QT_TRANSLATE_NOOP("utabit-core", "Maximum per-connection receive buffer, <n>*1000 bytes (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Maximum per-connection send buffer, <n>*1000 bytes (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Minimum bytes per sigop in transactions we relay and mine (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Need to specify a port with -whitebind: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Node relay options:"),
QT_TRANSLATE_NOOP("utabit-core", "Not enough file descriptors available."),
QT_TRANSLATE_NOOP("utabit-core", "Only connect to nodes in network <net> (ipv4, ipv6 or onion)"),
QT_TRANSLATE_NOOP("utabit-core", "Options:"),
QT_TRANSLATE_NOOP("utabit-core", "Password for JSON-RPC connections"),
QT_TRANSLATE_NOOP("utabit-core", "Prepend debug output with timestamp (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Print version and exit"),
QT_TRANSLATE_NOOP("utabit-core", "Prune cannot be configured with a negative value."),
QT_TRANSLATE_NOOP("utabit-core", "Prune mode is incompatible with -txindex."),
QT_TRANSLATE_NOOP("utabit-core", "Pruning blockstore..."),
QT_TRANSLATE_NOOP("utabit-core", "RPC server options:"),
QT_TRANSLATE_NOOP("utabit-core", "Rebuild block chain index from current blk000??.dat files on startup"),
QT_TRANSLATE_NOOP("utabit-core", "Receive and display P2P network alerts (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Reducing -maxconnections from %d to %d, because of system limitations."),
QT_TRANSLATE_NOOP("utabit-core", "Relay and mine data carrier transactions (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Relay non-P2SH multisig (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Rescan the block chain for missing wallet transactions on startup"),
QT_TRANSLATE_NOOP("utabit-core", "Rescanning..."),
QT_TRANSLATE_NOOP("utabit-core", "Run in the background as a daemon and accept commands"),
QT_TRANSLATE_NOOP("utabit-core", "Send trace/debug info to console instead of debug.log file"),
QT_TRANSLATE_NOOP("utabit-core", "Send transactions as zero-fee transactions if possible (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Set database cache size in megabytes (%d to %d, default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", "Set key pool size to <n> (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Set maximum block size in bytes (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", "Set minimum block size in bytes (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Set the number of threads to service RPC calls (default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", "Show all debugging options (usage: --help -help-debug)"),
QT_TRANSLATE_NOOP("utabit-core", "Shrink debug.log file on client startup (default: 1 when no -debug)"),
QT_TRANSLATE_NOOP("utabit-core", "Signing transaction failed"),
QT_TRANSLATE_NOOP("utabit-core", "Specify configuration file (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Specify connection timeout in milliseconds (minimum: 1, default: %d)"),
QT_TRANSLATE_NOOP("utabit-core", "Specify data directory"),
QT_TRANSLATE_NOOP("utabit-core", "Specify pid file (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Specify wallet file (within data directory)"),
QT_TRANSLATE_NOOP("utabit-core", "Specify your own public address"),
QT_TRANSLATE_NOOP("utabit-core", "Spend unconfirmed change when sending transactions (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "The transaction amount is too small to pay the fee"),
QT_TRANSLATE_NOOP("utabit-core", "This help message"),
QT_TRANSLATE_NOOP("utabit-core", "This is experimental software."),
QT_TRANSLATE_NOOP("utabit-core", "Threshold for disconnecting misbehaving peers (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "Tor control port password (default: empty)"),
QT_TRANSLATE_NOOP("utabit-core", "Tor control port to use if onion listening enabled (default: %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Transaction amount too small"),
QT_TRANSLATE_NOOP("utabit-core", "Transaction amounts must be positive"),
QT_TRANSLATE_NOOP("utabit-core", "Transaction too large for fee policy"),
QT_TRANSLATE_NOOP("utabit-core", "Transaction too large"),
QT_TRANSLATE_NOOP("utabit-core", "Unable to bind to %s on this computer (bind returned error %s)"),
QT_TRANSLATE_NOOP("utabit-core", "Unable to start HTTP server. See debug log for details."),
QT_TRANSLATE_NOOP("utabit-core", "Unknown network specified in -onlynet: '%s'"),
QT_TRANSLATE_NOOP("utabit-core", "Unsupported argument -benchmark ignored, use -debug=bench."),
QT_TRANSLATE_NOOP("utabit-core", "Unsupported argument -debugnet ignored, use -debug=net."),
QT_TRANSLATE_NOOP("utabit-core", "Unsupported argument -tor found, use -onion."),
QT_TRANSLATE_NOOP("utabit-core", "Upgrade wallet to latest format on startup"),
QT_TRANSLATE_NOOP("utabit-core", "Use UPnP to map the listening port (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "User Agent comment (%s) contains unsafe characters."),
QT_TRANSLATE_NOOP("utabit-core", "Username for JSON-RPC connections"),
QT_TRANSLATE_NOOP("utabit-core", "Verifying blocks..."),
QT_TRANSLATE_NOOP("utabit-core", "Verifying wallet..."),
QT_TRANSLATE_NOOP("utabit-core", "Wallet %s resides outside data directory %s"),
QT_TRANSLATE_NOOP("utabit-core", "Wallet needed to be rewritten: restart Utabit Core to complete"),
QT_TRANSLATE_NOOP("utabit-core", "Wallet options:"),
QT_TRANSLATE_NOOP("utabit-core", "Warning"),
QT_TRANSLATE_NOOP("utabit-core", "Warning: unknown new rules activated (versionbit %i)"),
QT_TRANSLATE_NOOP("utabit-core", "Whether to operate in a blocks only mode (default: %u)"),
QT_TRANSLATE_NOOP("utabit-core", "You need to rebuild the database using -reindex to change -txindex"),
QT_TRANSLATE_NOOP("utabit-core", "Zapping all transactions from wallet..."),
QT_TRANSLATE_NOOP("utabit-core", "ZeroMQ notification options:"),
QT_TRANSLATE_NOOP("utabit-core", "wallet.dat corrupt, salvage failed"),
};
