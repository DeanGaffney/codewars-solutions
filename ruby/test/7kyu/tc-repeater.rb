require "test/unit"
require_relative "../../src/7kyu/repeater.rb"

class RepeaterTest < Test::Unit::TestCase
    def test_repeater
        assert_equal(Repeater.new().repeater('a', 5), 'aaaaa')
        assert_equal(Repeater.new().repeater('Na', 16), 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa')
        assert_equal(Repeater.new().repeater('Wub ', 6), 'Wub Wub Wub Wub Wub Wub ')
    end
end