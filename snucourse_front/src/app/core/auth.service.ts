import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { HttpErrorService } from './http-error.service';
import { catchError, tap, delay } from 'rxjs/operators';
import { Router } from '@angular/router';
import { LectureService } from './lecture.service';

export const TOKEN_KEY = 'access_token';
export function tokenGetter() {
  return localStorage.getItem(TOKEN_KEY);
}

export interface SignUpPayload {
  email: string;
  name: string;
  student_id: number;
  password: string;
  major: string;
  double_major: string;
  minor: string;
}

export interface AuthResponse {
  name: string;
  token: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(
    private http: HttpClient,
    private errorHandler: HttpErrorService,
    private router: Router,
    private lecture: LectureService
  ) {}
  user;
  graduate;
  redirectUrl: string;

  get token() {
    return tokenGetter();
  }

  get isLoggedIn(): boolean {
    return !!this.token;
  }

  setToken(token: string) {
    localStorage.setItem(TOKEN_KEY, token);
  }

  login(email: string, password: string): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>('/user/login/', { username: email, password })
      .pipe(
        tap(({ token }) => this.setToken(token)),
        tap(() => this.router.navigate(['/'])),
        catchError(this.errorHandler.handleError)
      );
  }

  signup(payload: SignUpPayload): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>('/user/signup/', payload)
      .pipe(
        tap(({ token }) => this.setToken(token)),
        tap(() => this.router.navigate(['/'])),
        catchError(this.errorHandler.handleError)
      );
  }

  registerCourses() {
    // http post request for registering courses then navigate to /
    return of(null).pipe(
      delay(1000),
      tap(() => this.router.navigate(['/'])),
      catchError(this.errorHandler.handleError)
    );
  }

  logout() {
    localStorage.removeItem(TOKEN_KEY);
    this.router.navigate(['intro']);
  }

  getUser() {
    return this.http.get('/user/info').pipe(
      tap((user: any) => {
        this.user = user;
        console.log('user: ', user);
        this.lecture.alreadyReviewed = user.lecture_opinions.map(
          opinion => opinion.lecture.id
        );
        console.log('alreadyReviewed: ', this.lecture.alreadyReviewed);
      })
    );
  }

  getGraduateAssessment() {
    return this.http
      .get('/user/graduate_assessment')
      .pipe(tap(graduate => (this.graduate = graduate)), tap(console.log));
  }
}
