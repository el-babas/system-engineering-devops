# Install a package - Using Puppet, install puppet-lint.

package { 'puppet_lint':
    ensure   => '2.5.0',
    name     => 'puppet-lint',
    provider => 'gem',
    source   => 'http://rubygems.org',
}
