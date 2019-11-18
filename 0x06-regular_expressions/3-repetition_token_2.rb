#!/usr/bin/env ruby
txt = ARGV
puts txt[0].scan(/hbt{1,}n/).join
