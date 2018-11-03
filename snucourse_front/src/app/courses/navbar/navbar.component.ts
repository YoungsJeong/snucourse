import { Component, OnInit, Input } from '@angular/core';
import { AuthService } from '../../core/auth.service';
import { Router } from '@angular/router';
import { NgbDropdownConfig } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  @Input() name: string;
  constructor(
    public auth: AuthService,
    private router: Router,
    private config: NgbDropdownConfig
  ) {
    config.placement = 'bottom-right';
  }

  ngOnInit() {}

  goToProfile() {
    this.router.navigate(['profile']);
  }

  goToHome() {
    this.router.navigate(['/']);
  }
}
