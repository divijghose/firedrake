Installation failure with Firedrake on MacOS. I opened `firedrake-install.log` and saw the error message `Error configuring SUPERLU_DIST with CMake`. 

**Solution**

Begin by confirming your Xcode version with the terminal command `xcodebuild -version`. If the response is `Xcode 15.0`, upgrading from Xcode 15 to Xcode 15.1 is a potential solution. Xcode 15.1 is available at the Apple Store.