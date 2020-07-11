import anybadge

# Define thresholds: <2=red, <4=orange <8=yellow <10=green
thresholds = {
    2: 'red',
    4: 'orange',
    6: 'yellow',
    10: 'green'
}

coverage = anybadge.Badge('coverage', 56, thresholds=thresholds)
coverage.write_badge('.badges/coverage.svg')

build = anybadge.Badge('build', 'pass', thresholds=thresholds)
build.write_badge('.badges/build.svg')