{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs?release-24.11";

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        yarn
        nodejs_23
      ];
    };
  };
}