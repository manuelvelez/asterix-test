import time
import os

from lettuce import before
from lettuce import after


@before.each_scenario
def say_hello(feature):
    print "Hello test"
    
@after.all
def report(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_passed,
        total.scenarios_ran
    )
