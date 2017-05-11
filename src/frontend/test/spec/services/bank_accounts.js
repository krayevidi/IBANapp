'use strict';

describe('Service: bankAccounts', function () {

  // load the service's module
  beforeEach(module('frontendApp'));

  // instantiate service
  var bankAccounts;
  beforeEach(inject(function (_bankAccounts_) {
    bankAccounts = _bankAccounts_;
  }));

  it('should do something', function () {
    expect(!!bankAccounts).toBe(true);
  });

});
