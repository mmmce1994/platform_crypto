![ƀ](/images/icon.png) utabitwallet for Android
----------------------------------

[![download](/images/icon-google-play.png)](https://play.google.com/store/apps/details?id=com.utabitwallet)

### What is Utabit?

Utabit is an experimental digital currency that enables instant payments to
anyone, anywhere in the world. Utabit uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network. Utabit Core is the name of open source
software which enables the use of this currency.

For more information, as well as an immediately useable, binary version of
the Utabit Core software, see http://utabit.com/#download, or read the
[original whitepaper](http://utabit.com/?page_id=6091).

### utabit done right

This is the Android port of the utabitwallet iOS app, which can be found [here](https://github.com/utabit/utabitwallet-ios/).

##### a completely standalone utabit wallet:

Unlike many other utabit wallets, utabitwallet is a real standalone utabit
client. There is no server to get hacked or go down, so you can always access
your money. Using
[SPV](https://en.utabit.it/wiki/Thin_Client_Security#Header-Only_Clients)
mode, utabitwallet connects directly to the utabit network with the fast
performance you need on a mobile device.

##### the next step in wallet security:

utabitwallet is designed to protect you from malware, browser security holes,
*even physical theft*. With AES hardware encryption, app sandboxing, and verified boot, utabitwallet represents a significant security advance over
web and desktop wallets.

##### beautiful simplicity:

Simplicity is utabitwallet's core design principle. A simple backup phrase is
all you need to restore your wallet on another device if yours is ever lost or
broken.  Because utabitwallet is  
[deterministic](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki),
your balance and transaction history can be recovered from just your backup
phrase.

### features:

- ["simplified payment verification"](https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki) for fast mobile performance
- no server to get hacked or go down
- single backup phrase that works forever
- private keys never leave your device
- import [password protected](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) paper wallets
- ["payment protocol"](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki) payee identity certification

## How to set up the development environment:
1. Download and install Java 7 or up
2. Download and Install the latest Android studio
3. Download and install the latest NDK https://developer.android.com/ndk/downloads/index.html or download it in android studio by "choosing the NDK" and press "download"
4. Go to https://github.com/utabit/utabitwallet-android and clone or download the project
5. Open the project with Android Studio and let the project sync
6. Go to SDK Manager and download all the SDK Platforms and SDK Tools
7. Initialize the submodules - <code>git submodule init</code>
8. Update the submodules - <code>git submodule update</code>
9. Build -> Rebuild Project
