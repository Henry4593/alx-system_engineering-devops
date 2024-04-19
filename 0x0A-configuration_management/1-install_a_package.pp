# Install Flask with specific version (2.1.0) using pip3 provider
package { 'flask':
  ensure   => '==2.1.0',
  provider => 'pip3',
}
