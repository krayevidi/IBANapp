'use strict';

describe('Controller: BankAccountsListCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var BankAccountsListCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BankAccountsListCtrl = $controller('BankAccountsListCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(BankAccountsListCtrl.awesomeThings.length).toBe(3);
  });
});
