{ pkgs }: {
  deps = [
    # \/ for pyqt5 or pyqt4, change 6 to 5 or 4 
    pkgs.python310Packages.pyqt6
  ];
}