#!/usr/bin/env ruby
txt = ARGV
puts txt[0].scan(/hbt{2,5}n/).join
