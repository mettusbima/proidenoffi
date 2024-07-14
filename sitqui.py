import pkg_resources

def check_compatibility(requirements_file='requirements.txt'):
    # Read the requirements file
    with open(requirements_file, 'r') as f:
        requirements = f.readlines()

    # Loop through each requirement and check its version
    for req in requirements:
        req = req.strip()
        if req:
            try:
                # Parse the requirement
                package = pkg_resources.Requirement.parse(req)
                # Get the installed distribution
                installed_dist = pkg_resources.get_distribution(package.project_name)
                # Check if the installed version satisfies the requirement
                if installed_dist not in package:
                    print(f'Incompatible version for {package.project_name}: '
                          f'{installed_dist.version} (required: {package.specifier})')
                else:
                    print(f'{package.project_name} is compatible: '
                          f'{installed_dist.version}')
            except pkg_resources.DistributionNotFound:
                print(f'{package.project_name} is not installed.')
            except pkg_resources.VersionConflict as e:
                print(e)

# Run the compatibility check
check_compatibility()
