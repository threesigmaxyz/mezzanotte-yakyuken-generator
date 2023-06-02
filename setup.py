from setuptools import setup, find_packages

package_name = 'yakyuken'
package_version = '1.0.0'

setup(
    name=package_name,
    version=package_version,
    author='Three Sigma',
    author_email='info@threesigma.xyz',
    description='Mezzanotte Yakyuken NFT Generator',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'yakyuken = yakyuken.__main__:cli',
        ],
    },
)
