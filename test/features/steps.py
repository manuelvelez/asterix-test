# -*- coding: utf-8 -*-

# System dependences
import time
from lettuce import step


@step(u'Given the terrain is fine')
def given_the_terrain_is_fine(step):
    time.sleep(5)

@step(u'When asterix runs "([^"]*)"')
def when_asterix_runs_group1(step, group1):
    print "Asterix is fucking running. Why doesn't he stop?"

@step(u'Then the terray is a bit messy')
def then_the_terray_is_a_bit_messy(step):
    assert False, 'This step must be implemented'
