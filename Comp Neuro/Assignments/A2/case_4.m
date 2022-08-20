%% Case 4 
% (a)
% I1 = 0.740 A and I2 = 0.259 A. 

a = 0.5;
b = 0.02;
r = 0.5;

I_ext = 0.00;
dt = 0.01
[v0, w0] = meshgrid([-1:0.25:1.5]);
figure(1);

% nullclines
v1 = [-1:0.1:1.5];
w1 = [-1:0.1:1.5];
v_null = (v1.*(a-v1).*(v1-1)) + I_ext;
w_null = (b/r)*v1;
%% (b) and (c)
% The steady states are at three points, approximately: 
% (0.0, 0.0), (0.6, 0.024) and (0.9, 0.036)
% nullclines


%perturbation from fixed point steady state-(1.014, 0.01267)
[v_phase,w_phase] = fhn(I_ext,0.9+1, 0.036,a,b,r);

subplot(1,2,1)
% For v0 = 1 we plot the response versus time curves
time=0:0.05:100;
plot(time,v_phase);
hold on
ylabel({'V'});
xlabel({'time (s)'});
title({'V vs time'});

subplot(1,2,2)
plot(time,w_phase);
ylabel({'W'});
xlabel({'time (s)'});
title({'W vs time'});
