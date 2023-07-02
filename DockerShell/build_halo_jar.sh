CRTDIR=$(pwd)
cd ~
mkdir tmp_halo_build
cd ./tmp_halo_build

git clone git@github.com:halo-dev/halo.git
cd ./halo
git checkout -b release-1.6 origin/release-1.6
./gradlew clean build -x check

cp ./build/libs/halo-1.6.0-SNAPSHOT.jar ${CRTDIR}/
cd ${CRTDIR}
