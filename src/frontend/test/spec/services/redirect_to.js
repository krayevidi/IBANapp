'use strict';

describe('Service: redirectTo', function () {

  // load the service's module
  beforeEach(module('frontendApp'));

  // instantiate service
  var redirectTo;
  beforeEach(inject(function (_redirectTo_) {
    redirectTo = _redirectTo_;
  }));

  it('should do something', function () {
    expect(!!redirectTo).toBe(true);
  });

});
