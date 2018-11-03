import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface DepartmentSearchResponse {
  id: string;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class LectureService {
  alreadyReviewed = [];
  constructor(private http: HttpClient) {}

  searchDepartment(search: string): Observable<DepartmentSearchResponse[]> {
    const params = new HttpParams().set('q', search);
    return this.http.get<DepartmentSearchResponse[]>('/search/department', {
      params
    });
  }

  writeOpinion(payload) {
    return this.http.post('/lecture/write_opinion/', payload);
  }

  getLectureDetail(id: string) {
    return this.http.get(`/lecture/${id}/`);
  }

  searchLectrue({
    type,
    department,
    lecturer,
    creditTotal,
    area,
    name,
    grade
  }) {
    let params = new HttpParams();
    if (type) {
      params = params.set('type', type);
    }
    if (department) {
      params = params.set('department', department);
    }
    if (name) {
      params = params.set('name', name);
    }
    if (lecturer) {
      params = params.set('lecturer', lecturer);
    }
    if (grade) {
      params = params.set('grade', grade);
    }
    if (creditTotal) {
      params = params.set('credit_Total', creditTotal);
    }
    if (area) {
      params = params.set('area', area);
    }
    return this.http.get('/search/lecture_detail', { params });
  }
}
